import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_model(data):
    df = data.copy()
    df['workout_done'] = LabelEncoder().fit_transform(df['workout_done'])
    X = df[['water_intake', 'sleep_hours', 'screen_time']]
    y = df['workout_done']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model