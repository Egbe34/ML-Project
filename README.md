# ML-Project

## Introduction



- 🛠 GitHub Repository: [ML-Project](https://github.com/Jessica-Bu/ML-Project)
- 📋 Trello Board: [Project Tasks & Timeline](https://trello.com/b/CNv59pX7/project-week-7) 
- Presentation: [Stroke](https://docs.google.com/presentation/d/.../view) 

## Datasets Used

We use 1 file with raw data.
 *  **Stroke data (healthcare-dataset):** Demographics like age, gender, and account details of Vanguard's clients.

At the same time, we were provided with a Metadata(dictionary) to help us understand the content of the columns in each file and guide us through the analysis

* **id:** Every client's unique ID.
* **gendr:** Specifies the client's gender.
* **age:** Indicates the age of the client.
* **hypertension:** High blood pressure (Yes/No)
* **heart_disease:** Issue with heart (Yes/No)
* **ever_married:** Marital status (Yes/No)
* **work\_type:** Employment status (Private/Self-employed/Govt\_job/children/Never\_worked).
* **Residence_type:** Living area (Urban/Rural).
* **avg\_glucose\_level:** Average glucose level in blood.
* **bmi:** Body Mass Index.
* **smoking_status:** Smoking status (never smoked/formerly smoked/Unknown/smokes)
* **stroke:** Stroke status (True/False)


**Comments on the Data:**

* **Main Challenges:** 
* **Strengths:** 
* **Weaknesses:** 

##  Business Problem & Hypothesis
Create Machine Learning model to predict stroke based on patient's symtoms

* **Question:** 
* **Conclusion:**  

_*Business recommendation*_: 

## Methodology

Our methodology involved several key steps, focusing on data preprocessing, ML-Model selection, Model training , Model evaluation, and tuning

1.  **Data preprocessing:** 
    * Datasets were downloaded from kaggle.
    * Data Cleaning: 
        * maping categorical values to numerical, drop "id" column, not considering gender "Other"
        * fillna bmi with average value
2.  **Model selection:** 
3.  **Model training:**  

4.  **Model evaluation:** 

5.  **Model tuning:**

6.  **Insights:**

  **Data Analysis Tools and Libraries:**
* __Python__: The primary programming language for data manipulation and analysis.
* __Pandas__:Essential for data loading, cleaning, and transformation.
* __Matplotlib / Seaborn__: Used for creating various visualizations (bar charts, line graphs).

##  Repository Structure

```
proj-vanguard-abtest/
├── data/                        # Raw and cleaned CSV files
├── figures/                     # Sketching of structure in dataset
├── notebooks/                   # Python notebooks with analysis
├── README.md                    # This file
└── slides                       # Url of presentation
```
## 👥 Team Members
__*Robert, Jessica, Guilherme, Egbe*__