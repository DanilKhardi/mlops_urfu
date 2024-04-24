import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Загрузка модели
    model = joblib.load('./data/model/model.pkl')

    # Загрузка тестовых данных
    test_data = pd.read_csv('./data/test/test_water_level_preprocessed.csv')
    x_test, y_test = test_data[['day']], test_data['water_level']

    # Предсказание и оценка модели
    predictions = model.predict(x_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error for the test set: {mse}')

    # Создание графика
    # predictions - это предсказанные значения уровня воды
    # y_test - это реальные значения уровня воды
    plt.figure(figsize=(10, 6))
    plt.plot(x_test, y_test, label='Real Water Levels', color='blue')
    plt.plot(x_test, predictions, label='Predicted Water Levels', color='red')

    # Настройка графика
    plt.title('Water Level Prediction')
    plt.xlabel('Day')
    plt.ylabel('Water Level')
    plt.legend()

    # Сохранить график
    plt.savefig("./data/model/plot.png", dpi=360)
    # plt.show()
