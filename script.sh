#!/bin/sh

if [ ! -f credit_model.pkl ]; then
    python train_model.py
fi

flask run --host=0.0.0.0 --port=5000