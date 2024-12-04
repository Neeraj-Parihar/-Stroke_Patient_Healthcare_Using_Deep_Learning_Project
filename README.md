Stroke Prediction Using Machine Learning
Project Overview
This project utilizes machine learning models to predict the likelihood of stroke occurrence in individuals. The work is organized into several key milestones:

Milestone 1: Data Preprocessing
Milestone 2: Data Visualization & Analysis
Milestone 3: Data Encoding
Milestone 4: Model Building, Evaluation, and Metrics Calculation (Precision, Accuracy, F1-Score)
Milestone 5: UI Development Using Streamlit
Key Features
Data Preprocessing:

Cleaned the dataset by handling missing values and ensuring consistency across entries.
Addressed the class imbalance issue within the dataset.
Data Visualization:

Explored patterns and correlations between features using visual tools.
Created visualizations to analyze class distribution and identify significant attributes influencing stroke risk.
Data Encoding:

Transformed categorical variables into numerical formats using one-hot encoding and label encoding.
Machine Learning Models:

Built multiple models, including Ridge Regression, Lasso Regression, Logistic Regression, and Linear Regression.
Evaluated model performance through metrics such as precision, recall, F1-score, and accuracy.
User Interface with Streamlit:

Developed a simple and interactive UI using Streamlit.
Added a Generate button, which, when clicked, displays the predicted result based on the model.
Dataset Overview
<u>Key Features:</u>

Target Variable: Stroke occurrence (binary: 0 = No Stroke, 1 = Stroke).
Class Imbalance: 95% of the instances are labeled as "No Stroke," while 5% are labeled as "Stroke."
Features: Includes variables like age, gender, BMI, hypertension, etc.
Challenges Faced
Class Imbalance:
The dataset is imbalanced, making it difficult for models to detect stroke cases.
Metric Selection:
Accuracy alone was not sufficient due to the imbalance; recall and F1-score were emphasized for a better evaluation of stroke detection.
Milestone Breakdown
Milestone 1: Data Preprocessing
Cleaned the dataset by handling missing values and scaling numerical features.
Milestone 2: Data Visualization
Explored and visualized the dataset to understand the distribution of classes and correlations among features.
Milestone 3: Data Encoding
Applied one-hot encoding and label encoding to transform categorical variables.
Normalized features to improve model performance.
Milestone 4: Model Building & Evaluation
Built and evaluated Ridge, Lasso, Logistic, and Linear Regression models.
Performance Insights:
Achieved high accuracy (92.46%) but struggled with stroke detection due to poor recall.
F1-scores highlighted the imbalance between precision and recall.
Milestone 5: UI Development with Streamlit
Created an interactive UI using Streamlit to visualize results.
Added a Generate button that triggers the model to predict stroke risk and display the result on the webpage.
Future Directions
Class Balancing:

Implement techniques such as SMOTE or undersampling to address class imbalance.
Model Enhancements:

Experiment with more sophisticated models like Random Forest, XGBoost, or ensemble methods to improve prediction accuracy and recall.
Feature Engineering:

Derive additional features from existing data to boost model performance and make predictions more reliable.
🎯 Goal: Improve stroke prediction accuracy and assist healthcare providers in early detection with more reliable models and tools.












