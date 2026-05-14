if [ ! -f credit_model.pkl ]; then
    python train_model.py
fi

python app.py