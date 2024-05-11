import pandas as pd

df = pd.read_csv('../datasets/titanic_dataset.csv')

# One-hot-encoding for Sex feature
ohe = pd.get_dummies(df['Sex'], prefix='Sex')

df = pd.concat([df, ohe], axis=1)

df.to_csv('../datasets/titanic_dataset.csv', index=False)