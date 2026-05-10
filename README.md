# Introduction to Artificial Intelligence

This repository contains the material for the **Introduction to Artificial Intelligence** course aimed at undergraduate students. The course introduces the theoretical and practical foundations of Machine Learning and Artificial Intelligence through guided tutorials, model-focused exercises, and real-world applications.

---

## Course Structure

The course is organized into **thematic units**, each including:

- **Tutorials**: End-to-end machine learning pipelines for realistic problems.  
- **Practicals**: Focused exercises for deepening understanding of specific models.  
- **Web Applications**: Deployment of trained models using Flask.

---

## Units

### Unit 1: Python for data science and linear models

All notebooks live in `unidad_1/` and are meant to be followed **in numerical order**.

- **Topics**: Python basics; NumPy, Pandas, and visualization; pipeline ideas (generalization, underfitting, overfitting); linear and logistic regression in realistic settings  
- **Models**: ordinary least squares / linear regression, logistic regression (including multiclass)  
- **Extras**: optional Flask deployment (`app.py`)

**Notebooks:**

| Order | Notebook | Description |
|-------|----------|-------------|
| 1 | `unidad_1/00.variables_python.ipynb` | Types, collections, conditionals, loops |
| 2 | `unidad_1/01.exploring_numpy.ipynb` | NumPy arrays, stats, linear algebra |
| 3 | `unidad_1/02.exploring_pandas.ipynb` | DataFrames, manipulation, I/O |
| 4 | `unidad_1/03.exploring_matplotlib.ipynb` | Matplotlib and Seaborn |
| 5 | `unidad_1/04.simple_pipeline.ipynb` | First ML pipeline: errors, generalization, overfitting |
| 6 | `unidad_1/05.life_expectancy.ipynb` | Regression: life expectancy by country |
| 7 | `unidad_1/06.house_pricing.ipynb` | Regression: housing prices (Santiago metropolitan region) |
| 8 | `unidad_1/07.star_classification.ipynb` | Multiclass classification: stellar types (SDSS) |
| — | `unidad_1/app.py` | Web app serving a trained regression model |

**Datasets** (paths are relative to the repo root; place files under `datasets/` as in each notebook):

| Notebook | Dataset / source |
|----------|------------------|
| `05.life_expectancy.ipynb` | `datasets/LifeExpectancy.csv` (bundled; [Life Expectancy (WHO) on Kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who) is a common public variant) |
| `06.house_pricing.ipynb` | `datasets/2023-03-08 Precios Casas RM.csv`; similar open data: [Used houses RM Chile](https://www.kaggle.com/datasets/gorkigonzalez/casas-usadas-rm-chile-mayo-2020) |
| `07.star_classification.ipynb` | `datasets/star_classification.csv` — [Stellar Classification SDSS17](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17) |

---

### Unit 2: Linear algebra, PCA, and classical classifiers

All notebooks live in `unidad_2/` and are meant to be followed **in numerical order**.

- **Math**: vector spaces, finite-dimensional spaces, linear maps (matrices, kernel/range, determinants, change of basis)  
- **Supervised learning**: logistic regression with **PCA** on digits; **KNN**; **decision trees**; **random forests**; **Multinomial Naive Bayes** on text  
- **Probability**: Bayes’ theorem and sequential belief updating (`06.bayes.ipynb`)

**Notebooks:**

| Order | Notebook | Description |
|-------|----------|-------------|
| 1 | `unidad_2/00.vector_spaces.ipynb` | Axioms and geometry of vector spaces |
| 2 | `unidad_2/01.finite-dimensional_vector_spaces.ipynb` | Bases, dimension, coordinates |
| 3 | `unidad_2/02.linear_maps.ipynb` | Matrices as maps; kernel, range, inverse; basis change |
| 4 | `unidad_2/03.digit_recognition.ipynb` | EDA, scaling, logistic regression, **PCA**, MNIST-style digits |
| 5 | `unidad_2/04.alzheimer_classification.ipynb` | EDA, feature engineering, **KNN** |
| 6 | `unidad_2/05.music_recognizer.ipynb` | **KNN**, **decision tree**, **random forest** for music genres |
| 7 | `unidad_2/06.bayes.ipynb` | Bayes theorem: priors, likelihood, posteriors |
| 8 | `unidad_2/07.spam_detection.ipynb` | Text features, **MultinomialNB**, optional **t-SNE** |

**Datasets:**

| Notebook | Dataset |
|----------|---------|
| `03.digit_recognition.ipynb` | [Digit Recognizer (MNIST)](https://www.kaggle.com/c/digit-recognizer) |
| `04.alzheimer_classification.ipynb` | `datasets/alzheimer/alzheimer.csv` — [Alzheimer Features](https://www.kaggle.com/datasets/brsdincer/alzheimer-features) |
| `05.music_recognizer.ipynb` | `data.csv` in the notebook folder — [Music features](https://www.kaggle.com/datasets/insiyeah/musicfeatures) |
| `07.spam_detection.ipynb` | `datasets/SPAM text message 20170820 - Data.csv` — [Spam text message classification](https://www.kaggle.com/datasets/team-ai/spam-text-message-classification) |


---

### Unit 3: Deep Learning

- **Multilayer Perceptron**
- **Transfer learning and Fine tuning**


**Notebooks:**

- `practico_1.ipynb`: Use a model, apply transfer learning and finetuning.
- `practico_2.ipynb`: Basic concepts of dense neural networks.

**Datasets:**

| Notebook           | Dataset                                                                                     |
|--------------------|---------------------------------------------------------------------------------------------|
| `practico_1.ipynb` | [Cats and Dogs](https://www.kaggle.com/datasets/marquis03/cats-and-dogs)                    |
| `practico_2.ipynb` | Simulated data                                                                              |
| `practico_3_CNN.ipynb` | CIFAR-10 (imported directly from the notebook)                                                                             |

---

## Requirements

Install Python 3 and the following libraries:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn flask joblib nltk
```
Install torch following the instructions of [Get Started](https://pytorch.org/get-started/locally/)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
You may also want:

- Jupyter Notebook or JupyterLab
- VSCode
- `venv` or `conda` for environment management

---

## How to Use This Repository

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

## Author and Contributions

This course was created by **Gabriel Cabas** for undergraduate students beginning their journey in Artificial Intelligence.  
Contributions, feedback, and pull requests are welcome!

---

## License

This repository is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and share the content with appropriate attribution.
