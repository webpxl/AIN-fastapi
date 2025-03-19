from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import numpy as np
import pandas as pd
import joblib
import random

def clean_transform_df(df, model_columns=None):    
    df = df.copy()
    df = df.set_index('PassengerId')
    
    # Extract titles
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

    # Standardize titles
    title_mapping = {'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'}
    df['Title'] = df['Title'].replace(title_mapping)

    # Create mask for title replacement
    title_mask = ~df['Title'].isin(['Mr', 'Miss', 'Mrs', 'Master'])
    df.loc[title_mask, 'Title'] = df.loc[title_mask, 'Sex'].map({'male': 'Mr', 'female': 'Mrs'})
    
    # Medians for main titles collected previously manually
    title_age_medians = {
        'Mr': 32.32,
        'Miss': 21.68,
        'Mrs': 35.86,
        'Master': 4.57
    }
    
    # Fill age based on title medians
    for title, median_age in title_age_medians.items():
        age_mask = (df['Age'].isnull()) & (df['Title'] == title)
        df.loc[age_mask, 'Age'] = median_age

    # Replace inplace fillna operations
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())

    df['Age*Class'] = df['Age'] * df['Pclass']
    df['Age*Fare'] = df['Age'] * df['Fare']    

    df_sex = pd.get_dummies(df['Sex'], prefix='sex', drop_first=True, dtype=int)
    df_Pclass = pd.get_dummies(df['Pclass'], prefix='class', drop_first=True, dtype=int)
    df_Embarked = pd.get_dummies(df['Embarked'], prefix='Embarked', drop_first=True, dtype=int)
    df_Title = pd.get_dummies(df['Title'], prefix='Title', drop_first=False, dtype=int)

    df = pd.concat([df, df_sex, df_Pclass, df_Embarked, df_Title], axis=1)

    # Family features
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # Fare and Age bands
    df['AgeBand'] = pd.cut(df['Age'], bins=[0, 12, 20, 40, 60, np.inf], labels=[0, 1, 2, 3, 4])
    df['AgeBand'] = df['AgeBand'].astype(int)
  
    df['FareBand'] = pd.cut(df['Fare'], bins=[0,10,25,100,np.inf], labels=[0, 1, 2, 3])
    #df['FareBand'] = pd.qcut(df['Fare'], q=4, labels=[0, 1, 2, 3])
    df['FareBand'] = df['FareBand'].astype(int)
    
    # Log transformation
    df['Fare_log'] = np.log1p(df['Fare'])

    df = df.drop(['Sex','Pclass','Name','Ticket','Embarked','Cabin', 'Title','Fare', 'SibSp', 'Parch'], axis=1)

    # Reorder columns to match the expected column order
    # If model_columns is provided (i.e., columns used during training), we will ensure alignment.
    if model_columns:
        # Add missing columns
        missing_cols = set(model_columns) - set(df.columns)
        for col in missing_cols:
            df[col] = 0  # Add missing columns with zeros

        # Ensure all columns are in the same order as during training
        df = df[model_columns]

    return df

# Using https://www.kaggle.com/models/andreipaulavets/titanic-random-forest-0.794-score/
pkl_file = "titanic_model.pkl"
# Hard-coded column order
column_order = ['Age', 'Age*Class', 'Age*Fare', 'sex_male', 'class_2', 'class_3', 'Embarked_Q', 'Embarked_S', 'Title_Master', 'Title_Miss', 'Title_Mr', 'Title_Mrs', 'FamilySize', 'IsAlone', 'AgeBand', 'FareBand', 'Fare_log']

if os.path.exists(pkl_file):
    model = joblib.load(pkl_file)
else:
    print("File not found!")

app = FastAPI()

# Don't touch this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

class Passenger(BaseModel):
    PassengerId: int | None = None
    Name: str | None = None
    Sex: str | None = None
    Age: int | None = None
    Embarked: str | None = None
    Pclass: int | None = None
    Fare: float | None = None
    SibSp: int | None = None
    Parch: int | None = None
    Ticket: str | None = None
    Cabin: str | None = None

@app.post("/predict")
async def login(data: Passenger):
    
    # Convert the list of Pydantic models to a list of dictionaries
    passenger_dict = [passenger.dict() for passenger in [data]]
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(passenger_dict)

    features = clean_transform_df(df, model_columns=column_order)
    print('Features:', features.to_string())

    prediction = model.predict(features)
    print('Prediction:', prediction)
    return {"prediction": prediction.item()}