#!/usr/bin/env python3

from flask import Flask, request, render_template
from visuals import get_company_cocoa_percent
from model import classify_using_model

app = Flask("CacaoDemo")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cocoa-data")
def cocoa_data():
    return "%s" % get_company_cocoa_percent()

@app.route("/predict-cocoa-percent")
def predict_cocoa_percent():
    company =  request.args.get('company', '')
    company_location =  request.args.get('location', '')
    specific_bean_origin_or_bar_name =  request.args.get('origin', '')
    estimate  = classify_using_model(company,company_location,specific_bean_origin_or_bar_name)
    return "%.2f" % estimate


