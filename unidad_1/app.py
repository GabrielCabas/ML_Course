from flask import Flask, request, send_file
import os
import joblib #Importar joblib
import pandas as pd #Importar pandas


pipeline = joblib.load('model.job') #Cargar el modelo
app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stellar predictions</title>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" rel="stylesheet">
    </head>
    <body class="grey lighten-4">
        <div class="container">
            <div class="card-panel z-depth-3">
                <h5 class="blue-text text-darken-2">Upload a file to predict stellar classification</h5>
                <form action="/upload" method="post" enctype="multipart/form-data" target="uploadFrame" onsubmit="return handleFormSubmit(event)">
                    <div class="file-field input-field">
                        <div class="btn blue">
                            <span>Choose File</span>
                            <input type="file" name="file" id="file" required>
                        </div>
                        <div class="file-path-wrapper">
                            <input class="file-path validate" type="text" placeholder="Upload your file">
                        </div>
                    </div>
                    <button type="submit" class="btn blue">Predict</button>
                </form>
            </div>
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <script>
            async function handleFormSubmit(event) {
                event.preventDefault();
                const form = event.target;
                const formData = new FormData(form);
                try {
                    const response = await fetch(form.action, {
                        method: form.method,
                        body: formData
                    });
                    if (!response.ok) {
                        const errorData = await response.json();
                        M.toast({html: errorData.error, classes: 'red'});
                    } else {
                        const blob = await response.blob();
                        const url = window.URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.style.display = 'none';
                        a.href = url;
                        a.download = 'predictions.csv';
                        document.body.appendChild(a);
                        a.click();
                        window.URL.revokeObjectURL(url);
                        M.toast({html: 'File downloaded successfully!', classes: 'green'});
                    }
                } catch (error) {
                    M.toast({html: 'An unexpected error occurred', classes: 'red'});
                }
            }
        </script>
    </body>
    </html>
    '''
PROCESSED_FOLDER = 'processed'
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {"error": "No file part in the request"}, 400

    file = request.files['file']
    if file.filename == '':
        return {"error": "No selected file"}, 400
    file_path = request.files['file']
    X_test = pd.read_csv(file_path)  # Cargar el dataset de test directamente desde el archivo
    if X_test.empty:
        return {"error": "The uploaded file is empty"}, 400
    if set(pipeline.feature_names_in_).issubset(X_test.columns) == False:
        # Comprobar si las columnas del dataset de test son las mismas que las del dataset de entrenamiento
        return {"error": "The uploaded file does not have the same columns as the training data"}, 400
    X_test = X_test[pipeline.feature_names_in_].copy() #Filtrar las columnas del dataset de test
    y_pred = pipeline.predict(X_test) #Predecir el dataset de test
    y_prob = pipeline.predict_proba(X_test) #Predecir la probabilidad del dataset de test
    X_test['y_pred'] = y_pred
    X_test['y_prob'] = y_prob.max(axis = 1).round(3)
    processed_file_path = os.path.join(PROCESSED_FOLDER, 'predictions.csv')
    X_test.to_csv(processed_file_path, index=False)
    return send_file(processed_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)