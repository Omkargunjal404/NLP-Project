import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import csv
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("DATA", list(request.form.values()), list(request.form.keys()))
    listKeys = list(request.form.keys())
    listValues = list(request.form.values())

    data = {}
    data[listKeys[0]] = listValues[0]

    with open('drugsCom_raw (1).tsv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
    
        output = []
        for rows in csvReader:
            obj = {}
            obj['#'] = rows['']
            obj['DRUGNAME'] = rows['DRUGNAME']
            obj['CONDITION'] = rows['CONDITION']
            obj['SIDE_EFFECTS'] = rows['SIDE_EFFECTS']
            obj['EFFECTIVENESS'] = rows['EFFECTIVENESS']
            output.append(obj)
        
#     print(output)
        
        drugname = data['drugname']

        finalOut = []
        for item in output:
            if drugname != '' :
                if item['DRUGNAME'] == drugname:
                    finalOut.append(item)
            
                elif drugname == '':
                    print('enter the correct drug')
    return render_template('index.html', result=finalOut)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)