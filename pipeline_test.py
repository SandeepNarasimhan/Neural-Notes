from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import seaborn as sns
import pandas as pd
import numpy as np

# Load the Titanic dataset
df = sns.load_dataset("titanic")

# Drop rows with missing target
df = df.dropna(subset=["survived"])

# Define features and target
X = df[["pclass", "sex", "age", "fare", "embarked"]]
y = df["survived"]

class AgeGroup(BaseEstimator, TransformerMixin):
    def __init__(self, Age="age", AgeGroup="Age_Group"):
        self.Age= Age
        self.AgeGroup= AgeGroup

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X[self.AgeGroup] = pd.cut(X[self.Age], bins=[0,18,40,80, 100], labels=['<18', '18-40', '40-80', '80+'])
        return X

AgeGroup().fit_transform(X)

num_var = ['age', 'fare']
cat_var = ['pclass', 'sex', 'embarked', 'Age_Group']

num_pipeline = Pipeline([
    ("Standard_scale", StandardScaler())
])

cat_pipeline = Pipeline([
    ("OneHot", OneHotEncoder(drop=True, handle_unknown=True))
])

preprocessor = ColumnTransformer([
    ('Standard_scaler', StandardScaler(), num_var),
    ('OneHot', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_var)
])

pipeline = Pipeline([
    ("AgeGroup", AgeGroup()),
    ('preprocessor', preprocessor)
])

pipeline.fit_transform(X)
