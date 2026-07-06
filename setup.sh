#!/bin/bash

echo "🚀 AEON MATRIX BOOTSTRAP START"

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "🧠 Starting AEON MATRIX..."
uvicorn apps.api.server:app --host 0.0.0.0 --port 8000
