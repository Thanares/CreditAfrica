if [ ! -f filename ]; then
    python train_model.py
fi

python manage.py app.py