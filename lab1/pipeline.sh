#!/bin/bash

# Запуск Python-скриптов
scripts=("data_creation.py" "model_preprocessing.py" "model_preparation.py" "model_testing.py")

for script in "${scripts[@]}"; do
  if python "$script"; then
    echo "Script $script executed successfully."
  else
    echo "Error executing script $script"
    exit 1
  fi
done

echo "All scripts executed successfully."
