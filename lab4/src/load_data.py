import catboost.datasets as d

data, _ = d.titanic()
data.to_csv('../datasets/titanic_dataset.csv', index=False)