# 🤖 Introduction to Artificial Intelligence

This repository contains the material for the **Introduction to Artificial Intelligence** course aimed at undergraduate students. The course introduces the theoretical and practical foundations of Machine Learning and Artificial Intelligence through guided tutorials, model-focused exercises, and real-world applications.

---

## 🧭 Course Structure

The course is organized into **thematic units**, each including:

- 📘 **Tutorials**: End-to-end machine learning pipelines for realistic problems.  
- 🔬 **Practicals**: Focused exercises for deepening understanding of specific models.  
- 🌐 **Web Applications**: Deployment of trained models using Flask.

---

## 📚 Units

### ✅ Unit 1: Fundamentals, Linear Models, and Dimensionality Reduction

- **Topics**: risk minimization, generalization, underfitting, overfitting  
- **Models**: linear regression, logistic regression, Principal Component Analysis (PCA)  
- **Extras**: model deployment via Flask  

**Notebooks:**

- `simple_pipeline.ipynb`: Our first pipeline to understand some key concepts: generalization, overfitting, underfitting, error minimization, etc. 
- `guia_1.ipynb`: Introductory pipeline with housing prices dataset  
- `guia_1_extended.ipynb`: Extended version with additional features and improved model  
- `guia_2.ipynb`: Classification pipeline using astronomical data  
- `practico_1.ipynb`: Regression analysis on global temperature data  
- `practico_2.ipynb`: Logistic regression for university admission prediction  
- `practico_3.ipynb`: PCA on handwritten digits  
- `app.py`: Web application with a deployed regression model

**Datasets:**

| Notebook                   | Dataset                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| `guia_1.ipynb`, `extended` | [Used Houses RM Chile (May 2020)](https://www.kaggle.com/datasets/gorkigonzalez/casas-usadas-rm-chile-mayo-2020) |
| `guia_2.ipynb`             | [Stellar Classification SDSS17](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17) |
| `practico_1.ipynb`         | [Global Temperature Records](https://www.kaggle.com/datasets/maso0dahmed/global-temperature-records-1850-2022) |
| `practico_2.ipynb`         | [University Admission Chile](https://www.kaggle.com/datasets/daniellopez01/admisionuescl) |
| `practico_3.ipynb`         | [Digit Recognizer (MNIST)](https://www.kaggle.com/c/digit-recognizer) |

---

### 🧠 Unit 2: Clustering and Non-Parametric Classification Models

- **Unsupervised Learning**: K-Means, Agglomerative Clustering, DBSCAN, Gaussian Mixtures  
- **Supervised Learning**: Naive Bayes, K-Nearest Neighbors (KNN), Decision Trees, Random Forest  
- **Bayesian Reasoning**: Illustrations of the sequential nature of Bayes' theorem  

**Notebooks:**

- `guia_1.ipynb`: Clustering with four algorithms on the penguin dataset  
- `bayes_1.ipynb`, `bayes_2.ipynb`: Bayes theorem applied to toy examples  
- `practico_1.ipynb`: Naive Bayes for tweet sentiment classification  
- `practico_2.ipynb`: KNN classifier to predict Alzheimer's status

**Datasets:**

| Notebook           | Dataset                                                                                     |
|--------------------|---------------------------------------------------------------------------------------------|
| `guia_1.ipynb`     | [Clustering Penguins](https://www.kaggle.com/datasets/tentotheminus9/penguins)              |
| `practico_1.ipynb` | [Sentimental Analysis for Tweets](https://www.kaggle.com/datasets/gargmanas/sentimental-analysis-for-tweets) |
| `practico_2.ipynb` | [Alzheimer Features](https://www.kaggle.com/datasets/brsdincer/alzheimer-features)          |

---

## ⚙️ Requirements

Install Python 3 and the following libraries:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn flask
```

You may also want:

- Jupyter Notebook or JupyterLab
- VSCode
- `venv` or `conda` for environment management

---

## 🚀 How to Use This Repository

1. Clone the repository:

```bash
git clone https://github.com/GabrielCabas/ML_Course.git
cd ML_Course
```

2. Open the notebooks:

```bash
jupyter notebook
```

3. (Optional) Run web applications like `app.py`:

```bash
python unidad_1/app.py
```

---

## 🛠 Author and Contributions

This course was created by **Gabriel Cabas** for undergraduate students beginning their journey in Artificial Intelligence.  
Contributions, feedback, and pull requests are welcome!

---

## 📜 License

This repository is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and share the content with appropriate attribution.
