import pandas as pd

df = pd.read_csv('../datasets/titanic_dataset.csv')

# Replace Nan value on Mean age
df["Age"] = df['Age'].fillna(df['Age'].mean())

df.to_csv('../datasets/titanic_dataset.csv', index=False)