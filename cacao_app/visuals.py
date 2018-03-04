#!/usr/bin/env python

import pandas as pd 
import os
print("Current directory: ")

data_path=os.getcwd()+'/data/flavors_of_cacao.csv'



def get_cocoa_data():
    data = pd.read_csv(data_path)
    column_names = [ name.replace("-","").replace("\n","").replace(" ","").replace("\xa0","")  for name in data.columns]
    data.columns = column_names
    data['CocoaPercent']=data['CocoaPercent'].apply(lambda x : float(x.replace("%","")))
    return data



def get_company_cocoa_percent():
    data = get_cocoa_data()
    return data.groupby("Company(Makerifknown)")['CocoaPercent'].mean()

