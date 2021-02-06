from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import pandas as pd



app = Flask(__name__, template_folder='template')
model = pickle.load(open('ada_boost_classification_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


scaler = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Employee_ID=int(request.form['Employee_ID'])
        Age=int(request.form['Age'])
        Education=request.form['Education']
        if(Education=='High School'):
            Education=1
        elif(Education=='College'):
            Education=2
        elif(Education=='Bachelor"s Degree'):
            Education=3
        elif(Education=='Master"s Degree'):
            Education=4
        else:
            Education=5
        YearsAtCompany=int(request.form['YearsAtCompany'])
        MonthlyIncome=float(request.form['MonthlyIncome'])
        NumCompaniesWorked=int(request.form['NumCompaniesWorked'])
        StockOptionLevel=int(request.form['StockOptionLevel'])
        JobInvolvement=request.form['JobInvolvement']
        if(JobInvolvement=='Low'):
            JobInvolvement=1
        elif(JobInvolvement=='Medium'):
            JobInvolvement=2
        elif(JobInvolvement=='High'):
            JobInvolvement=3
        else:
            JobInvolvement=4
        TrainingTimesLastYear=int(request.form['TrainingTimesLastYear'])
        YearsSinceLastPromotion=int(request.form['YearsSinceLastPromotion'])
        YearsWithCurrManager=int(request.form['YearsWithCurrManager'])
        WorkLifeBalance=request.form['WorkLifeBalance']
        if(WorkLifeBalance=='Bad'):
            WorkLifeBalance=1
        elif(WorkLifeBalance=='Sufficient'):
            WorkLifeBalance=2
        elif(WorkLifeBalance=='Good'):
            WorkLifeBalance=3
        else:
            WorkLifeBalance=4
        JobSatisfaction=request.form['JobSatisfaction']
        if(JobSatisfaction=='Low'):
            JobSatisfaction=1
        elif(JobSatisfaction=='Medium'):
            JobSatisfaction=2
        elif(JobSatisfaction=='High'):
            JobSatisfaction=3
        else:
            JobSatisfaction=4
        EnvironmentSatisfaction=request.form['EnvironmentSatisfaction']
        if(EnvironmentSatisfaction=='Low'):
            EnvironmentSatisfaction=1
        elif(EnvironmentSatisfaction=='Medium'):
            EnvironmentSatisfaction=2
        elif(EnvironmentSatisfaction=='High'):
            EnvironmentSatisfaction=3
        else:
            EnvironmentSatisfaction=4
        OverTime=request.form['OverTime']
        if(OverTime=='Yes'):
            OverTime=1
        else:
            OverTime=0   
        features_list=[Age, Education, YearsAtCompany, MonthlyIncome, NumCompaniesWorked, StockOptionLevel, JobInvolvement, TrainingTimesLastYear, YearsSinceLastPromotion, YearsWithCurrManager, WorkLifeBalance, JobSatisfaction, EnvironmentSatisfaction, OverTime]
        features = np.asarray(features_list).reshape(1,-1)
        predictions= model.predict(features)
        output = predictions
        if output==0:
            return render_template('index.html',prediction_text="This employee will leave the company")
        else:
            return render_template('index.html',prediction_text="This employee will stay at the company")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

