from cmath import nan
import csv
import os
import string
from flask import Flask, Response, render_template, request
from flask_bootstrap import Bootstrap
from numpy import NaN
import re

import pandas as pd


def process(df, filename1):
    df['Code_Result'] = df.iloc[:,0].map(remapad)
    # df.to_excel("output.csv")

    output = df.to_csv(index=False)
    os.remove(filename1)
    return Response(
        output ,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename={}".format("after_" + filename1.replace('xlsx','csv'))})

def hasNum(str):
    return any(char.isdigit() for char in str)

def remapad(sentence) :
    final_addr = ""
    count = 0
    lis = ['flat','plot','survey','servey','apt','apartment','opposite','house','door']
    for x in sentence.split(","):
        if hasNum(str(x)) and count == 0:
            pass
        elif any(y in x.lower() for y in lis) :
            pass
        else:
            final_addr +=  x + ", "
        count += 1
    
#     x = re.findall('(\d+).*?\s+(.+)', sentence)
#     final_addr = ""
#     count = 0
#     for x in sentence.split(","):
#         if hasNum(x) and count == 0:
#             pass
#         elif "plot" in sentence.lower() or "flat" in sentence.lower() or "phase" in sentence.lower() or "survey" in sentence.lower() or "wing" in sentence.lower() or "gate" in sentence.lower() :
#             pass
#         else:
#             final_addr += x + ", "
#         count += 1
    return final_addr[:-2]

