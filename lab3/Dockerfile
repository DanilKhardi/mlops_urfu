# Создаем контейнер на основе Alpine Linux
FROM ubuntu:20.04

# Установка Python 3.10
RUN apt-get update && apt-get install -y python3 && ln -sf python3 /usr/bin/python


# Установка pip для управления пакетами Python
RUN apt-get install -y python3-pip

# Установка рабочей деректории
WORKDIR /app

# Копирование текущего каталога в контейнер
COPY . /app

# Установка зависимостей из файла
RUN pip install -r requirements.txt

# Запуск приложения
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
