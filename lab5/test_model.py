import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import  r2_score as r2


def get_data(dataset_name):
    DF = pd.read_csv(dataset_name)
    return pd.DataFrame(DF['X']), DF['y']


def test_dataset():
    X_train, y_train = get_data('dataset_1.csv')
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    for i in range(2, 5):
        X_test, y_test = get_data('dataset_' + str(i) + '.csv')
        MSE = mse(model.predict(X_test), y_test)
        assert MSE < 1, f"Датасет 'dataset_{str(i)}.csv' содержит неверные, MSE {MSE}!"
