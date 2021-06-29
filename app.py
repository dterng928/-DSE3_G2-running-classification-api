from flask import Flask, request, Response
import json
import pandas as pd
import numpy as np

import pickle

# tokenizer = RegexpTokenizer(r'[A-Za-z]+')
# snowball = SnowballStemmer("english")
# tfidVec = pickle.load(open('tfidVec_model.mod', 'rb'))
# loaded_model = pickle.load(open('svc_model.mod', 'rb'))

# def splitUrlIntoToken(url):
#     return tokenizer.tokenize(url)

# def removeTextFromList(input, rmTxt):
#     input = [x for x in input if (x not in rmTxt)]
#     return input

# def textNormByStemType(inputTxt, stemtype):
#     inputTxt =[stemtype.stem(word) for word in inputTxt]
#     return inputTxt

app = Flask(__name__)

@app.route('/')
def homePage():
    return """<xmp>To check Runner Type.
Example use api by '/racing_type?active=ไม่เคย'</xmp>"""

def recommendRacing(answer):
    # print(answer)
    if answer :
        # print('in switcher')
        switcher = {
            'ไม่เคย': '10km',
            'น้อยกว่า 25 กิโล': '10km',
            '25-35 กิโล': '21km',
            '35 กิโลขึ้นไป': '42km',
        }
        for key, value in switcher.items():
            if key in answer:
                return switcher.get(key, 'ไม่มีรายการแนะนำในช่วงนี้')
    # print('not in if')
    return 'ไม่มีรายการแนะนำในช่วงนี้'

@app.route('/racing_type', methods=['GET'])
def getRacingType():
    print(request.args)
    result = recommendRacing(request.args['active']) if 'active' in request.args else 'ไม่มีรายการแนะนำในช่วงนี้'
    
    print('recommend racing: ', result)
    
    res = Response(json.dumps({'raceType':result}))
    res.headers['response-type'] = 'intent'
    res.headers['Content-Type'] = 'application/json; charser=utf-8'
    return res
    # return json.dumps({'raceType':result})

if __name__ == "__main__":
    app.run(threaded=True)