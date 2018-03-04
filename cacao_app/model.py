#!/usr/bin/env python 

import os
from sklearn.externals import joblib
import pandas as pd

model_path = os.getcwd()+'/data/model.pkl'
encoder_path = os.getcwd()+'/data/encoders.data'

def import_model():
	clf = joblib.load(model_path)
	return clf

def import_encoders():
	encoders = joblib.load(encoder_path)
	return encoders

def classify_using_model(company,company_location,specific_bean_origin_or_bar_name): 
	encoders = import_encoders()
	print("Data Received Company='%s', Location='%s', Origin='%s'" % (company, company_location, specific_bean_origin_or_bar_name) )
	print("Encoder")
	print(encoders['Company(Makerifknown)'])
	company = encoders['Company(Makerifknown)'].transform([company])
	company_location = encoders['CompanyLocation'].transform([company_location])
	specific_bean_origin_or_bar_name = encoders['SpecificBeanOriginorBarName'].transform([specific_bean_origin_or_bar_name])
	print("Data transformed Company='%s', Location='%s', Origin='%s'" % (company, company_location, specific_bean_origin_or_bar_name) )
	model = import_model()
	prediction = model.predict(pd.DataFrame([[company,company_location,specific_bean_origin_or_bar_name]]))
	return prediction[0]


