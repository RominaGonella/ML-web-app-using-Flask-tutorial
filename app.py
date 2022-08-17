from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import numpy as np

# creamos objeto flask
app = Flask(__name__) # __name__ es alias de nombre del archivo

# se carga el modelo
loaded_model = pickle.load(open('coffee_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

#prediction function
def ValuePredictor(to_predict_list):
    cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']
    to_predict = pd.DataFrame(np.array(to_predict_list).reshape(1,8), columns = cols)
    result = loaded_model.predict(to_predict)
    return result.tolist()[0]

@app.route('/result/', methods = ['POST'])
def result():
    to_predict_list = [x for x in request.form.values()]
    print(to_predict_list)
    result = ValuePredictor(to_predict_list)
    print(result)

    if result == 'Yes':
        prediction = 'Yes it is a specialty coffee'
    else:
        prediction = 'It is not a specialty coffee'

    return render_template("index.html", prediction = prediction)

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)
