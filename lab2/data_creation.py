import numpy as np
import pandas as pd
import os


def generate_water_level_dataset(years=1, noise_std=0.5):
    """
    Функция генерирует датасет описывающий изменение уровня воды в реке в течение года.

    Параметры:
    - years: количество лет данных для генерации
    - noise_std: стандартное отклонение шума, добавляемого к данным

    Возвращает:
    - days: массив дней в году
    - water_levels: массив уровня воды в метрах
    """

    np.random.seed(42)  # Установка начального значения для генератора случайных чисел
    days_per_year = 365
    total_days = years * days_per_year
    days = np.arange(1, total_days + 1)

    # Генерация базового уровня воды, имитирующего сезонные колебания
    base_water_level = np.sin(days / days_per_year * 2 * np.pi) * 5 + 10

    # Добавление шума для имитации случайных колебаний уровня воды
    water_levels = base_water_level + np.random.normal(scale=noise_std, size=total_days)

    return days, water_levels


if __name__ == "__main__":
    # Генерация тренировочного и тестовго датасета
    YEARS = 2
    train_days, train_water_levels = generate_water_level_dataset(years=YEARS, noise_std=0.25)
    test_days, test_water_levels = generate_water_level_dataset(years=YEARS, noise_std=0.75)

    # Сохранение данных в csv-файлы
    os.makedirs("lab2/data/train", exist_ok=True)
    os.makedirs("lab2/data/test", exist_ok=True)
    pd.DataFrame({"day": train_days, "water_level": train_water_levels}). \
        to_csv(os.path.join("lab2/data/train", "train_water_level_dataset.csv"), index=False)
    pd.DataFrame({"day": test_days, "water_level": test_water_levels}). \
        to_csv(os.path.join("lab2/data/test", "test_water_level_dataset.csv"), index=False)
