# streamlit_mlp_app.py
import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load your MLP model
with open('trained_random_forest_model.sav', 'rb') as model_file:
    mlp_model = pickle.load(model_file)

# Function to make predictions
def make_prediction(user_input):
    # Use the loaded model to make predictions
    prediction = mlp_model.predict(user_input)
    return prediction

# Streamlit UI
def main():
    st.title('Random Forest model Deployment with Streamlit')

    # Sidebar description
    st.sidebar.header('Description')
    st.sidebar.write(
        "This is a Streamlit app for predicting employee attrition using an Random Forest model. "
        "____, and click 'Predict' to get the model's prediction."
    )

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
        'Age': [Age],
        'DailyRate': [DailyRate],
        'DistanceFromHome': [DistanceFromHome],
        'HourlyRate': [HourlyRate],
        'MonthlyIncome': [MonthlyIncome],
        'MonthlyRate': [MonthlyRate],
        'NumCompaniesWorked': [NumCompaniesWorked],
        'PercentSalaryHike': [PercentSalaryHike],
        'TotalWorkingYears': [TotalWorkingYears],
        'TrainingTimesLastYear': [TrainingTimesLastYear],
        'YearsAtCompany': [YearsAtCompany],
        'YearsInCurrentRole': [YearsInCurrentRole],
        'YearsSinceLastPromotion': [YearsSinceLastPromotion],
        'YearsWithCurrManager': [YearsWithCurrManager],
        'OverTime_Yes': [1 if OverTime == 'YES' else 0],
        'JobRole_HumanResources': [1 if JobRole == 'Human Resources' else 0],
        'JobRole_LaboratoryTechnician': [1 if JobRole == 'Laboratory Technician' else 0],
        'JobRole_Manager': [1 if JobRole == 'Manager' else 0],
        'JobRole_ManufacturingDirector': [1 if JobRole == 'Manufacturing Director' else 0],
        'JobRole_ResearchDirector': [1 if JobRole == 'Research Director' else 0],
        'JobRole_ResearchScientist': [1 if JobRole == 'Research Scientist' else 0],
        'JobRole_SalesExecutive': [1 if JobRole == 'Sales Executive' else 0],
        'JobRole_SalesRepresentative': [1 if JobRole == 'Sales Representative' else 0],
        'JobLevel_2': [1 if JobLevel == 2 else 0],
        'JobLevel_3': [1 if JobLevel == 3 else 0],
        'JobLevel_4': [1 if JobLevel == 4 else 0],
        'JobLevel_5': [1 if JobLevel == 5 else 0],
        'StockOptionLevel_1': [1 if StockOptionLevel == 1 else 0],
        'StockOptionLevel_2': [1 if StockOptionLevel == 2 else 0],
        'StockOptionLevel_3': [1 if StockOptionLevel == 3 else 0],
        'MaritalStatus_Married': [1 if MaritalStatus == 'Married' else 0],
        'MaritalStatus_Single': [1 if MaritalStatus == 'Single' else 0],
        'JobInvolvement_2': [1 if JobInvolvement == 2 else 0],
        'JobInvolvement_3': [1 if JobInvolvement == 3 else 0],
        'JobInvolvement_4': [1 if JobInvolvement == 4 else 0],
        'BusinessTravel_Travel_Frequently': [1 if BusinessTravel == 'Travel_Frequently' else 0],
        'BusinessTravel_Travel_Rarely': [1 if BusinessTravel == 'Travel_Rarely' else 0],
        'EnvironmentSatisfaction_2': [1 if EnvironmentSatisfaction == 2 else 0],
        'EnvironmentSatisfaction_3': [1 if EnvironmentSatisfaction == 3 else 0],
        'EnvironmentSatisfaction_4': [1 if EnvironmentSatisfaction == 4 else 0],
        'JobSatisfaction_2': [1 if JobSatisfaction == 2 else 0],
        'JobSatisfaction_3': [1 if JobSatisfaction == 3 else 0],
        'JobSatisfaction_4': [1 if JobSatisfaction == 4 else 0],
        'WorkLifeBalance_2': [1 if WorkLifeBalance == 2 else 0],
        'WorkLifeBalance_3': [1 if WorkLifeBalance == 3 else 0],
        'WorkLifeBalance_4': [1 if WorkLifeBalance == 4 else 0],
        'Department_Research&Development': [1 if Department == 'Research & Development' else 0],
        'Department_Sales': [1 if Department == 'Sales' else 0],
        'EducationField_LifeSciences': [1 if EducationField == 'Life Sciences' else 0],
        'EducationField_Marketing': [1 if EducationField == 'Marketing' else 0],
        'EducationField_Medical': [1 if EducationField == 'Medical' else 0],
        'EducationField_Other': [1 if EducationField == 'Other' else 0],
        'EducationField_TechnicalDegree': [1 if EducationField == 'Technical Degree' else 0],
    })

    # Make predictions
    if st.button('Predict'):
        user_input_array = user_input.values.reshape(1, -1)
        prediction = make_prediction(user_input_array)

        # Interpret the prediction
        if prediction[0] == 0:
            prediction_text = "Not likely to leave"
        else:
            prediction_text = "Likely to leave"

        st.write('Prediction:', prediction_text)


# Run the Streamlit app
if __name__ == '__main__':
    main()
