#!/bin/sh
venv="lenv"
python -m venv "$venv"
source "$venv/bin/activate"

pip install numpy pandas matplotlib seaborn