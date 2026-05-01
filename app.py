from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('credit_model.pkl')

def credit_score(probability_of_default):
    score = round((1 - probability_of_default) * 100, 1)
    
    if score >= 75:
        label = "Faible risque"
        recommandation = "Crédit recommandé"
        couleur = "green"
    elif score >= 50:
        label = "Risque modéré"
        recommandation = "Crédit possible avec garanties"
        couleur = "orange"
    else:
        label = "Risque élevé"
        recommandation = "Crédit déconseillé"
        couleur = "red"
    
    return {"score": score, "label": label,
            "recommandation": recommandation, "couleur": couleur}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    
    input_data = {
        "RevolvingUtilizationOfUnsecuredLines": float(data['revolving']),
        "age": int(data['age']),
        "NumberOfTime30-59DaysPastDueNotWorse": int(data['retard_30']),
        "DebtRatio": float(data['debt_ratio']),
        "MonthlyIncome": float(data['income']),
        "NumberOfOpenCreditLinesAndLoans": int(data['open_credits']),
        "NumberOfTimes90DaysLate": int(data['retard_90']),
        "NumberRealEstateLoansOrLines": int(data['real_estate']),
        "NumberOfTime60-89DaysPastDueNotWorse": int(data['retard_60']),
        "NumberOfDependents": int(data['dependents'])
    }
    
    df = pd.DataFrame([input_data])
    proba = model.predict_proba(df)[0][1]
    resultat = credit_score(proba)
    
    return render_template('resultat.html', resultat=resultat, data=data)

if __name__ == '__main__':
    print("Démarrage du serveur...")
    app.run(debug=True, port=5000)
    