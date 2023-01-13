from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__)
filename = 'file_iris.pkl'
model = pickle.load(open(filename, 'rb'))
#model = joblib.load(filename)
#model = joblib.load(filename)
@app.route('/')


def index(): 
    return render_template('index.html')
@app.route('/predict', methods=['POST'])


def predict():
    Sepal_Length = request.form['sepal_length']
    Sepal_Width = request.form['sepal_width']
    Petak_Length = request.form['petal_length']
    Petal_Width = request.form['petal_width']
    Sepal-perimeter_worst = request.form['perimeter_worst']
    radius_worst  = request.form['radius_worst
    concave_points_mean = request.form['concave_points_mean']
    area_worst = request.form['area_worst']
    perimeter_mean = request.form['perimeter_mean']
    area_mean = request.form['area_mean']
    radius_mean = request.form['radius_mean']
    area_se = request.form['area_se']
    concavity_worst = request.form['concavity_worst']
    radius_se = request.form['radius_se']
    compactness_worst = request.form['compactness_worst']
    perimeter_se = request.form['perimeter_se']
    compactness_mean = request.form['compactness_mean']

    
      
    pred = model.predict(np.array([[perimeter_worst,radius_worst,concave_points_mean,
                                    area_worst,perimeter_mean,area_mean,radius_mean,area_se,
                                    concavity_worst, radius_se, compactness_worst,perimeter_se,
                                    compactness_mean ]]))
    print(pred)
    return render_template('index.html', predict=str(pred))


if __name__ == '__main__':
    app.run
