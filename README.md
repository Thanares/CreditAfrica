# 💳 CreditAfrica

> Système de scoring de crédit par IA pour les institutions financières africaines



![Python](https://img.shields.io/badge/Python-3.13-blue)




![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey)




![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)



---

## 🎯 Problème

Plus de 80% des africains n'ont pas accès au crédit formel faute d'historique bancaire.
Les institutions prennent leurs décisions sur la base de l'intuition.

## 💡 Solution

CreditAfrica analyse des données financières simples et génère
un score de crédit 0-100 en quelques secondes grâce au Machine Learning.

---

## ⚙️ Stack technique

| Couche | Technologie |
|--------|-------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Machine Learning | scikit-learn, Random Forest |

---

## 🤖 Modèle ML

- Dataset : Give Me Some Credit - 150 000 profils
- Algorithme : Random Forest Classifier
- Performance : AUC-ROC 0.835

---

## 🚀 Lancer le projet

Installer les dépendances :

    pip install flask scikit-learn pandas joblib

Générer le modèle :

    python train_model.py

Lancer l'application :

    python app.py

Ouvrir http://127.0.0.1:5000 dans le navigateur.

---

## 🌍 Vision

Le modèle peut être réentraîné sur des données africaines locales :

- 📱 Mobile Money — MTN, Orange, Wave
- 🤝 Tontines et Njangi — discipline financière communautaire
- 📞 Téléphonie — ancienneté et régularité de recharge
- 🏪 Commerce local — historique fournisseurs

---

## 👥 Équipe

Projet réalisé dans le cadre du Hackathon IA · Finance Africaine

---

## 📄 Licence

MIT License