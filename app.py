from flask import Flask, render_template, request
import joblib
import pandas as pd
from flask_mysqldb import MySQL

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Thanares-07'
app.config['MYSQL_DB'] = 'creditafrica'

mysql = MySQL(app)
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

    # Sauvegarde en base
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO evaluations 
        (age, revenu, debt_ratio, score, label, recommandation)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        input_data['age'],
        input_data['MonthlyIncome'],
        input_data['DebtRatio'],
        resultat['score'],
        resultat['label'],
        resultat['recommandation']
    ))
    mysql.connection.commit()
    cur.close()

    return render_template('resultat.html', resultat=resultat, data=data)

@app.route('/historique')
def historique():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM evaluations ORDER BY date_evaluation DESC")
    evaluations = cur.fetchall()
    cur.close()
    return render_template('historique.html', evaluations=evaluations)

if __name__ == '__main__':
    print("Démarrage du serveur...")
    app.run(debug=True, port=5000)