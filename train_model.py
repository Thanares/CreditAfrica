import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv('data/cs-training.csv')
df = df.drop(columns=['Unnamed: 0'])
df['MonthlyIncome'] = df['MonthlyIncome'].fillna(df['MonthlyIncome'].median())
df['NumberOfDependents'] = df['NumberOfDependents'].fillna(df['NumberOfDependents'].median())

X = df.drop(columns=['SeriousDlqin2yrs'])
y = df['SeriousDlqin2yrs']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)
joblib.dump(model, 'credit_model.pkl')
print("Modèle sauvegardé !")


features = X.columns
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

for i in range(len(features)):
    print(f"{features[indices[i]]}: {importances[indices[i]]:.4f}")

