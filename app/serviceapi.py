import logging
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/getRowsdata')
def getRowsdata():
    rows = request.args.get('row')
    print(rows)
    rows =int(rows)
    import pandas as pd
    readfile = pd.read_excel('app/books.xlsx')
    df = pd.DataFrame(readfile)
    js = df.to_json(orient = 'records')

    
    with open("app/books.json", "w+") as outfile:
        outfile.write(js)


    jsonFile = open("app/books.json",)
    data = json.load(jsonFile)
    return jsonify(data=data[:rows])
    

@app.route('/getRequestedKeydata')
def getRequestedKeydata():
    keyvalue = request.args.get('KeyValue')
    keyvalue = json.loads(keyvalue)
    key =list(keyvalue.keys())
    value = keyvalue[key[0]]
    import pandas as pd
    readfile = pd.read_excel('app/books.xlsx')
    df = pd.DataFrame(readfile)
    js = df.to_json(orient = 'records')

    
    with open("app/books.json", "w+") as outfile:
        outfile.write(js)


    jsonFile = open("app/books.json",)
    data = json.load(jsonFile)
    if(data[0].get(key[0])):
        for x in data:
            if x[key[0]] == value:
                return x
    else:
        return "Key does not exist"


