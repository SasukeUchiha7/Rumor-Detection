from flask import Flask, render_template, request
import joblib
from preprocess import *

pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def rumor_detection():

    result = request.form
    title = result['title']
    author = result['author']
    text = result['text']
    total = concate(title,author,text)
    query = cleaning(total)
    query=[query]
    prediction = pipeline.predict(query)
    res=prediction[0]
    return render_template('index.html', result=res)


if __name__ == '__main__':
    app.run()