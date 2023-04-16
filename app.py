from flask import Flask, render_template
import random
import joblib
import itertools
import numpy as np
import tensorflow as tf
import scipy.stats

app = Flask(__name__, static_url_path='/static')
string = ""
scores = []
loaded_model = tf.keras.models.load_model('model')
print (loaded_model.summary())

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def addVariables(array):
    string_array = ''.join([str(x) for x in array])
    for i in itertools.product(*[('0', '1')] * 6): # considers all five-length strings
        array.append(string_array.count(''.join(i)))
    array.append(sum(array[:50]))
    return array

def toBinary(s):
    binary = []
    for i in s:
        if i == "1":
            binary.append(0)
        else:
            binary.append(1)
    return binary

@app.route('/updatescore')
def updateScore():
    global loaded_model
    if len(string) < 50:
        return "-1"
    summer = 0
    while len(scores)+49 < len(string):
        a = np.array([addVariables(toBinary(string[len(scores):len(scores)+50]))])
        print (a)
        value = loaded_model.predict(a)
        scores.append(value)
    return str((sum(scores)/len(scores))[0,0])

@app.route('/')
def index():
    global string 
    string = ""
    return render_template('index.html')

@app.route('/append/<string:word>')
def append(word):
    if not word.isnumeric():
        return "-1"
    if len(set([i for i in word]) - set(['1', '2'])) > 0:
        return "-1"
    global string
    string += word
    return string

@app.route('/toss')
def toss():
    global string
    result = str(random.randint(1, 2))
    string += result
    return string

@app.route('/coin-tosses')
def tossten():
    global string
    for i in range(10):
        result = str(random.randint(1, 2))
        string += result
    return string

@app.route('/clear')
def clear():
    global scores
    scores = []
    global string
    string = ""
    return string

if __name__ == '__main__':
    app.run()
