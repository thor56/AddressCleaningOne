# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

import csv
import os
import string
from flask import Flask, Response, render_template, request
from flask_bootstrap import Bootstrap4
from numpy import NaN
from requests_html import HTMLSession
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from CustomFunctions import *
import pandas as pd
 
# Flask constructor takes the name of
# current module (__name__) as argument.
# set FLASK_ENV=development
# set FLASK_APP = "app"

app = Flask(__name__)
bootstrap = Bootstrap4(app)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template("index.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
    filename = ""
    if request.method == 'POST':
        f = request.files['csvfile']
        if f.filename == '':
            f = request.files['csvfile1']
        f.save( f.filename)
        filename = f.filename
        df = pd.read_excel(f.filename, engine="openpyxl")
        #(df)
        return process(df, filename)
    return "None"
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)