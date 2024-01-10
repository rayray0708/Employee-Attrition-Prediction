# Employee-Attrition-Prediction
![Employee Attrition](https://whatfix.com/blog/wp-content/uploads/2022/09/employee-churn.png)

## Introduction
Employee retention strategies are integral to the success and well-being of a company. There are often many reasons why employees leave an organization, and in this case study, we will explore some of the key drivers of employee attrition. Employee attrition measures how many 
workers have left an organization and is a common metric companies use to assess their performance. While turnover rates vary from industry to industry, the Bureau of Labor Statistics reported that among voluntary separations the overall turnover rate was 25% in 2020.

In this project, we will explore IBM's dataset on HR Analytics. The data consists of nearly 1,500 current and former employees with information related to their job satisfaction, work life balance, tenure, experience, salary, and demographic data. Below is a brief overview and summary statistics of the data.

Objectives:
1. We would like to predict employee turnover and what are the 
relevant factors contributing to employee turnover.
2. Additionally, we would also want to predict job satisfaction and what
are the relevant factors contributing to low and high job satisfaction.

## Installations
The following dependancies have been installed for this project:
`import pandas as pd`
`from pathlib import Path`
`import matplotlib.pyplot as plt`
`from sklearn.model_selection import train_test_split`
`from sklearn.preprocessing import StandardScaler`
`import statsmodels.api as sm`
`from statsmodels.stats.outliers_influence import OLSInfluence`
`from sklearn.linear_model import LinearRegression`
`from sklearn.metrics import mean_squared_error, r2_score`

Please ensure you have these libraries pre-installed:
1) Scikit-learn: `!pip install scikit-learn`
2) Statsmodels: `!pip install statsmodels`
3) SQLAlchemy: `!pip install sqlalchemy`
4) Pandas: `!pip install pandas`
5) XGBoost: `pip install xgboost`

## Data extracting and cleaning
We retrieved our dataset from Kaggle via this link: https://www.kaggle.com/code/kellibelcher/hr-analytics-and-prediction-of-employee-attrition

Our dataset contains the following columns:
1. `Age`
2. `Attrition`
3. `BusinessTravel`
4. `DailyRate`
5. `Department`
6. `DistanceFromHome`
7. `Education`
8. `EducationField`
9. `EmployeeNumber`
10. `EnvironmentSatisfaction`
11. `Gender`
12. `HourlyRate`
13. `JobInvolvement`
14. `JobLevel`
15. `JobRole`
16. `JobSatisfaction`
17. `MaritalStatus`
18. `MonthlyIncome`
19. `MonthlyRate`
20. `NumCompaniesWorked`
21. `Over18`
22. `OverTime`
23. `PercentSalaryHike`
24. `PerformanceRating`
25. `RelationshipSatisfaction`
26. `StockOptionLevel`
27. `TotalWorkingYears`
28. `TrainingTimesLastYear`
29. `WorkLifeBalance`
30. `YearsAtCompany`
31. `YearsInCurrentRole`
32. `YearsSinceLastPromotion`
33. `YearsWithCurrManager`
34. `StandardHours`
35. `EmployeeCount`
![Alt text](<Screenshot 2024-01-04 at 9.14.56 pm.png>)
### Cleaning and generate summary stats

## Data loading
Demographic table
![Alt text](<Screenshot 2024-01-04 at 9.36.41 pm.png>)

Job table
![Alt text](<Screenshot 2024-01-04 at 9.37.49 pm.png>)


## Data modelling
### Predicting employee turnover using logistic regression
To delve deeper into our dataset and identify potential predictors of employee attrition, we employed a logistic regression model. This involved calculating odds ratios and p-values for all variables. While the overall model demonstrates statistical significance with a p-value of 3.363e-46, the Pseudo R-squared reveals a relatively low explanatory power, capturing only around 35% of the total variance in employee attrition. Refer to the model summary screenshot below for further details.
![Alt text](<Screenshot 2024-01-08 at 7.16.09 pm.png>)

### Predicting employee turnover using Multilayer Perceptron (MPL), XGBBoost and Random Forest
We decided that the initial logistic regression model served as a baseline model on which to modify and improve on. To improve the predictive power of our model as well as increasing the accuracy score, additional machine learning models were built: 1) a Multilayer Perceptron model, and 2) a Random Forest model. 

Our XGBoost MLP model achieved an overall high accuracy score of 84%. 
![Alt text](<Screenshot 2024-01-08 at 7.32.36 pm.png>)

To assess the association between Attrition and other categorical variables in the dataset, the chi-square test of independence was utilized. The null hypothesis posits that the variables are independent, indicating no discernible connection between Attrition and the variable under consideration. Conversely, the alternative hypothesis suggests the presence of a relationship.

The chi-square test was applied to each categorical column in the dataset. If the p-value resulting from the test was greater than or equal to 0.05, it implied that the variables were statistically independent. In such cases, these variables were considered for removal during the encoding process. The rationale behind this approach is that removing independent variables may contribute to enhancing the accuracy of the random forest algorithm. By refining the feature set, the algorithm can focus on more relevant predictors, potentially leading to improved predictive performance.
![Alt text](<Screenshot 2024-01-08 at 7.30.14 pm.png>) Random Forrest

Similarly, our Random Forest model achieved an overall impressive score of 86%. Based on this accuracy score, we've decided to use this model to build the Streamlit app. 

### Building the Streamlit app
To delpoy our Random Forest model, we utilised Streamlit. A screenshot of our Streamlit app is provided below. Please ensure you have the Streamlit app installed on your local machine by following the instructions below:
1) open your GitBash (on Windows) or Terminal (on Macs) and run this command line to install Streamlit: `pip install streamlit`.
2) navigate to App Directory: use the cd command to navigate to the directory where your Streamlit app script is located. E.g.,
![Alt text](<Screenshot 2024-01-08 at 8.27.47 pm.png>)
3) run Streamlit App: once you are in the correct directory, run the following command to launch your Streamlit app using the following command:
![Alt text](<Screenshot 2024-01-08 at 8.28.28 pm.png>)
Replace app.py with the name of your Streamlit app script if it has a different name.
4) Streamlit will prompt you answer some questions, please tab the key `return` (on Macs) or `enter` (on Windows) if you don't want to provide answers.
5) once you've done the previous steps, you should see the Streamlit app opening on a web browser, you can start interacting with the app.

A screenshot of what our Streamlit app looks like is provided below.
![Alt text](image.png)
