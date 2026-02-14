#!/bin/bash

echo "🔹 Activando entorno ATLAS..."

cd ~/atlas_v1 || exit
source venv/bin/activate

echo "🚀 Iniciando ATLAS..."
python3 principal.py
