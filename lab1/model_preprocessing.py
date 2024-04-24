from sklearn.preprocessing import StandardScaler
import pandas as pd


def read_data(path):
    return pd.read_csv(path)


def preprocessing(data, scaler):
    data["water_level"] = scaler.fit_transform(data[['water_level']])
    return data


def save_data(path, data):
    data.to_csv(path, index=False)


if __name__ == "__main__":
    # Загрузка данных
    train_data = read_data('./data/train/train_water_level_dataset.csv')
    test_data = read_data('./data/test/test_water_level_dataset.csv')

    # Предобработка данных
    scaler = StandardScaler()
    train_data = preprocessing(train_data, scaler)
    test_data = preprocessing(test_data, scaler)

    # Сохранение предобработанных данных
    save_data('./data/train/train_water_level_preprocessed.csv', train_data)
    save_data('./data/test/test_water_level_preprocessed.csv', test_data)
