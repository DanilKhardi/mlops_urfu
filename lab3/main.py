from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
import os
import joblib


# Маппинг индекса и названия класса ириса
IRIS_MAP = {"0": 'setosa', "1": 'versicolor', "2": 'virginica'}

class IrisParams(BaseModel):
    # Определяем входные параметры модели
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


def fit_model():
    if "iris_model.pkl" in os.listdir(os.path.join(os.getcwd(), "lab3/data")):
        # Загружаем модель из файла
        model, scaler = joblib.load("lab3/data/iris_model.pkl")
        return model, scaler
    else:
        # Обучаем модель
        # Загрузка датасета Iris
        iris = load_iris()
        X = iris.data
        y = iris.target

        # Сохранение в CSV
        iris_df = pd.DataFrame(X, columns=iris.feature_names)
        iris_df['target'] = y
        iris_df.to_csv('lab3/data/iris_dataset.csv', index=False)

        # Разделение данных на обучающую и тестовую выборки
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Выполняем предобработку данных
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Создание и обучение модели логистической регрессии
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train_scaled, y_train)

        # Записываем модель в файл
        with open('lab3/data/iris_model.pkl', 'wb') as file:
            pickle.dump((model, scaler), file)

        return model, scaler



app = FastAPI()
model, scaler = fit_model()


@app.get("/")
async def root():
    return {"message": str(type(model))}


@app.post("/predict/")
# Эндпоинт классификации ирисов
async def predict(item: IrisParams):
    input_data = [[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]]
    input_data_scaled = scaler.transform(input_data)
    try:
        prediction_index = str(model.predict(input_data_scaled)[0])
        if prediction_index in IRIS_MAP.keys():
            prediction_class = IRIS_MAP[prediction_index]
            return {"prediction_index": prediction_index, "prediction_class": prediction_class}
    except Exception as err:
        return {"prediction": "not identified"}

