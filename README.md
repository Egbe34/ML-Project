# ML-Project

## Introduction
A stroke is a medical emergency where blood flow to the brain is interrupted, causing brain cells to die due to lack of oxygen and nutrients. It’s a leading cause of death and disability worldwide but is often preventable and treatable with prompt action. Every minute a stroke goes untreated, ~1.9 million brain cells die.

Immediate action can save lives and reduce long-term disability. Awareness of symptoms and risk factors is critical.

- 🛠 GitHub Repository: [ML-Project](https://github.com/Jessica-Bu/ML-Project)
- 📋 Trello Board: [Project Tasks & Timeline](https://trello.com/b/CNv59pX7/project-week-7) 
- Presentation: [Stroke](https://docs.google.com/presentation/d/.../view) 

## Datasets Used

We use 1 file with raw data.
 *  **Stroke data (healthcare-dataset):** Demographics like age, gender, and account details of Vanguard's clients.

A Metadata(dictionary) is provided to help us understand the content of the columns in each file and guide us through the analysis

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
Predict stroke based on patient's health metrics to prevent stroke risk

* **Question:** 
* **Conclusion:**  

_*Business recommendation*_: 
  * This model can be used by hospitals and telehealth providers to screen patients quickly for stroke risk based on health metrics.
  * Helps prioritize care and perform early intervention in emergency.
  * Potential to integrate into electronic medical record (EMR) systems for real-time alerts.

## Methodology

Our methodology involved several key steps, focusing on data preprocessing, ML-Model selection, Model training , Model evaluation, and tuning

1.  **Data preprocessing:** 
    * Datasets were downloaded from kaggle.
    * Data Cleaning: 
        * maping categorical values to numerical, drop "id" column, not considering gender "Other"
        * fillna bmi with average value
2.  **EDA**
    * Age: Older patients have a significantly higher risk.
    * Hypertension & Heart Disease: Strong positive correlation with stroke.
    * Glucose Level & BMI: Higher values may indicate risk but with some variability.
    * Smoking Status: Formerly smoked and smokes groups show increased risk.   

3.  **Model selection:** 
    * KNN 
    * Logistic Regression
    * Random Forest

4.  **Model training:**  
* 
* 
* 

5.  **Model evaluation:** 

6.  **Model tuning:**

7.  **Insights:**

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