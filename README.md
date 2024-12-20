# Reddit Sentiment Analysis
**Course:** SENG 550: Scalable Data Analytics

## Objective
The goal of this project is to analyze how people's sentiments on climate change have changed over time. This project aims to identify the ongoing trend of climate change sentiment, as well as recognize important topics that spark engagement. 

## Group Members
- Monmoy Maahdie 
- Smitkumar Saraiya
- Farhan Ali
- Kai Ferrer

## Set Up
Before running this code, some set-up is required.

### Prerequisites
To run this project you need: 
- The Reddit Climate Change Dataset 
- Python 3.9+
- Jupyter Notebook 7.0+
- Installation of required dependencies using pip

### Reddit Climate Change Dataset
This dataset can be downloaded for free on Kaggle: https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset?resource=download.
Be sure to install this in the project root directory.

### Required pip installations
To run this project, you also need to install the required Python libraries.
- pandas, numpy, seaborn, scikit-learn, tensorflow, keras

Use the following command to install:

```bash
pip install pandas numpy seaborn scikit-learn tensorflow keras spacy pyspark nltk
```

Then, run
```bash
python -m spacy download en_core_web_sm
```

### Running using Jupyter Notebook
**In VS Code**
Ensure you have Jupyter Notebook extension installed in VS Code. Then, open the notebook (.ipynb) file within your project directory to run.

**In a browser**
Start Jupyter Notebook by running the following command in terminal:
```bash
jupyter notebook
```
or alternatively, go to http://localhost:8888/. Then, find your project's root directory to run the notebook.



