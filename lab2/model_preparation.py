import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor


def read_data(path):
    return pd.read_csv(path)


def save_model(path, model):
    os.makedirs("./data/model", exist_ok=True)
    joblib.dump(model, path)


if __name__ == "__main__":
    # Загрузка предобработанных данных
    data = read_data("./data/train/train_water_level_preprocessed.csv")
    x = data[["day"]]
    y = data["water_level"]

    # Разделение данных на обучающую и валидационную выборки
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=20, random_state=42)

    # Создание и обучение модели
    model = RandomForestRegressor(random_state=42)
    model.fit(x_train, y_train)

    # Сохранение модели
    joblib.dump(model, "./data/model/model.pkl")
    save_model("./data/model/model.pkl", model)
