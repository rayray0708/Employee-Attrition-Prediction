# streamlit_mlp_app.py
import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load your MLP model
with open('trained_mlp_model.sav', 'rb') as model_file:
    mlp_model = pickle.load(model_file)

# Function to make predictions
def make_prediction(user_input):
    # Use the loaded model to make predictions
    prediction = mlp_model.predict(user_input)
    return prediction

# Streamlit UI
def main():
    st.title('MLP Model Deployment with Streamlit')

    # User input
    DistanceFromHome = st.number_input('Distance from home')
    Education = st.slider('Education', 1, 4)
    EducationField = st.selectbox('Education Field', ('Life Sciences', 'Other', 'Medical', 'Marketing',
       'Technical Degree', 'Human Resources'))
    Age = st.number_input('Age')
    Gender = st.selectbox('Gender', ('Male', 'Female'))
    MaritalStatus = st.selectbox('Marital Status', ('Single', 'Married','Divorced'))
    Over18 = st.selectbox('Over 18',('Y',"N"))
    BusinessTravel = st.selectbox('Business Travel', ('Travel_Rarely', 'Travel_Frequently', 'Non-Travel'))
    DailyRate = st.number_input('Daily Rate')
    Department = st.selectbox('Department', ('Sales', 'Research & Development', 'Human Resources'))
    EnvironmentSatisfaction = st.slider('Environment Satisfaction', 1, 4)
    HourlyRate = st.number_input('Hourly Rate')
    MonthlyRate = st.number_input('Monthly Rate')
    MonthlyIncome = st.number_input('Monthly Income')
    JobInvolvement = st.slider('Job Involvement', 1, 4)
    OverTime = st.selectbox('Overtime', ('YES', 'NO'))
    JobLevel = st.slider('Job Level', 1, 5)
    JobRole = st.selectbox('Job Role',('Sales Executive', 'Research Scientist', 'Laboratory Technician',
       'Manufacturing Director', 'Healthcare Representative', 'Manager',
       'Sales Representative', 'Research Director', 'Human Resources'))
    JobSatisfaction = st.slider('Job Satisfaction', 1, 4)
    NumCompaniesWorked = st.number_input('Number of Companies Worked')
    PercentSalaryHike = st.slider('Salary Hike(Percent)', 1, 100)
    PerformanceRating = st.slider('Performance Rating', 1, 4)
    RelationshipSatisfaction = st.slider('Relationship Satisfaction', 1, 4)
    TotalWorkingYears = st.number_input('Total Working Years')
    StockOptionLevel = st.slider('Stock Option Level', 0, 3)
    TrainingTimesLastYear = st.number_input('Training Times Last Year')
    WorkLifeBalance = st.slider('Work Life Balance', 1, 4)
    YearsAtCompany = st.number_input('Years in Current Company')
    YearsInCurrentRole = st.number_input('Years in Current Role')
    YearsSinceLastPromotion = st.number_input('Years since last promotion')
    YearsWithCurrManager = st.number_input('Years with current manager')

    # Create a DataFrame with user input for one-hot encoding
    user_input = pd.DataFrame({
        'DistanceFromHome': [DistanceFromHome],
        'Education': [Education],
        'EducationField_Life Sciences': [1 if EducationField == 'Life Sciences' else 0],
        'EducationField_Other': [1 if EducationField == 'Other' else 0],
        'EducationField_Medical': [1 if EducationField == 'Medical' else 0],
        'EducationField_Marketing': [1 if EducationField == 'Marketing' else 0],
        'EducationField_Technical Degree': [1 if EducationField == 'Technical Degree' else 0],
        'EducationField_Human Resources': [1 if EducationField == 'Human Resources' else 0],
        'Age': [Age],
        'Gender_Female': [1 if Gender == 'Female' else 0],
        'Gender_Male': [1 if Gender == 'Male' else 0],
        'Marital_Status_Divorced': [1 if MaritalStatus == 'Divorced' else 0],
        'Marital_Status_Married': [1 if MaritalStatus == 'Married' else 0],
        'Marital_Status_Single': [1 if MaritalStatus == 'Single' else 0],
        'Over18_Y': [1 if Over18 == 'Y' else 0],
        'Business_Travel_Non-Travel': [1 if BusinessTravel == 'Non-Travel' else 0],
        'Business_Travel_Travel_Frequently': [1 if BusinessTravel == 'Travel_Frequently' else 0],
        'Business_Travel_Travel_Rarely': [1 if BusinessTravel == 'Travel_Rarely' else 0],
        'DailyRate': [DailyRate],
        'Department_Human Resources': [1 if Department == 'Human Resources' else 0],
        'Department_Research & Development': [1 if Department == 'Research & Development' else 0],
        'Department_Sales': [1 if Department == 'Sales' else 0],
        'EnvironmentSatisfaction': [EnvironmentSatisfaction],
        'HourlyRate': [HourlyRate],
        'MonthlyRate': [MonthlyRate],
        'MonthlyIncome': [MonthlyIncome],
        'JobInvolvement': [JobInvolvement],
        'JobLevel': [JobLevel],
        'JobSatisfaction': [JobSatisfaction],
        'NumCompaniesWorked': [NumCompaniesWorked],
        'PercentSalaryHike': [PercentSalaryHike],
        'PerformanceRating': [PerformanceRating],
        'RelationshipSatisfaction': [RelationshipSatisfaction],
        'StockOptionLevel': [StockOptionLevel],
        'TotalWorkingYears': [TotalWorkingYears],
        'TrainingTimesLastYear': [TrainingTimesLastYear],
        'WorkLifeBalance': [WorkLifeBalance],
        'YearsAtCompany': [YearsAtCompany],
        'YearsInCurrentRole': [YearsInCurrentRole],
        'YearsSinceLastPromotion': [YearsSinceLastPromotion],
        'YearsWithCurrManager': [YearsWithCurrManager],
        'Job_Role_Healthcare Representative': [1 if JobRole == 'Healthcare Representative' else 0],
        'Job_Role_Human Resources': [1 if JobRole == 'Human Resources' else 0],
        'Job_Role_Laboratory Technician': [1 if JobRole == 'Laboratory Technician' else 0],
        'Job_Role_Manager': [1 if JobRole == 'Manager' else 0],
        'Job_Role_Manufacturing Director': [1 if JobRole == 'Manufacturing Director' else 0],
        'Job_Role_Research Director': [1 if JobRole == 'Research Director' else 0],
        'Job_Role_Research Scientist': [1 if JobRole == 'Research Scientist' else 0],
        'Job_Role_Sales Executive': [1 if JobRole == 'Sales Executive' else 0],
        'Job_Role_Sales Representative': [1 if JobRole == 'Sales Representative' else 0],
        'Overtime_No': [1 if OverTime == 'NO' else 0],
        'Overtime_Yes': [1 if OverTime == 'YES' else 0]
    })

    # Make predictions
    if st.button('Predict'):
        user_input_array = user_input.values.reshape(1, -1)
        prediction = make_prediction(user_input_array)
        st.write('Prediction:', prediction[0])

# Run the Streamlit app
if __name__ == '__main__':
    main()
