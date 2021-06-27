from flask import Flask, request
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
Example use api by '/api?url=www.google.com'</xmp>"""

@app.route('/runner_type', methods=['GET'])
def getRunnerType():
    print(request.args)
    # phishingUrl = request.args['url']

    # splitText = splitUrlIntoToken(phishingUrl)
    # stemText = textNormByStemType(splitText, snowball)

    # data = ' '.join(stemText)
    # df = pd.DataFrame([data], columns = ['data'])

    # vectorText = tfidVec.transform(df['data'])

    # result = loaded_model.predict(vectorText)
    return request.args

if __name__ == "__main__":
    app.run(threaded=True)