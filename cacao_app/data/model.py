#!/usr/bin/env python 

import os
from sklearn.externals import joblib

model_path = os.getcwd()+'/data/model.pkl'

def import_model():
	clf = joblib.load(model_path)
	return clf

def classify_using_model(company,company_location,specific_bean_origin_or_bar_name): 
	
