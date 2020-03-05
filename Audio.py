from Feature import fft
from sklearn.svm import SVC
import numpy as np
import json
from flask import Flask
from flask import request
import time

app = Flask(__name__)

class audioRec:
    def __init__(self, path):
        self.clf = SVC(gamma='auto', probability=True, C=1)
        self.path = path

    def train(self):
        x, y = self.getdata(self.path)
        self.clf.fit(x, y)

    def test(self):
        x, y = self.getdata(self.path)
        print(self.clf.predict(x))
        print(y)
        print(self.clf.predict_proba(x))

    def predict(self, filename):
        features = fft(filename).getFFT()
        return self.clf.predict(features.reshape(1, -1)), self.clf.predict_proba(features.reshape(1, -1))

    def getdata(self, path):
        x = []
        y = []
        for line in open(path):  
            line = line.replace('\n', '').split(
                " ")  # delete /n, split by ','
            data = np.array(line)
            data = data.astype(np.int)
            x.append(data[:-1])
            y.append(data[-1])
            #print(data[-1])
        return x, y

@app.route('/animal')
def index():
    args = request.args
    print (args) # For debugging
    no1 = args['key']
    rec = audioRec("./ppig/data.txt")
    rec.train()
    Y, result = rec.predict("./ppig/labgg/" + no1 + ".wav")
    print(Y)
    a = 0
    mood = ["Normal", "Upset", "Angry"]
    localtime = time.asctime( time.localtime(time.time()) )
    for i in range(len(result[0])):
        if result[0][i] < result[0][a]:
            a = i
    
    #res = {"animal":"pig", "ourprediction": {"mood": mood[a], "score":result[0][a]}, "results":{"Normal": result[0][0],"Upset": result[0][1], "Angry": result[0][2]}, "time":localtime}
    res = {"animal":"pig", "ourprediction": {"mood": mood[int(Y[0])], "probability": 1-result[0][int(Y[0])]}, "probabilities":{"Normal": 1-result[0][0],"Upset": 1-result[0][1], "Angry": 1-result[0][2]}, "time":localtime}
    return json.dumps(res)
