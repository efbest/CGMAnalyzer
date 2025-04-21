#!/bin/bash

# Fehlerbehandlung: Skript bei Fehler abbrechen
set -e

# Wechsel ins Verzeichnis, in dem das Skript liegt
cd "$(dirname "$0")"

# Prüfe, ob python oder python3 verfügbar ist
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "Python ist nicht installiert. Bitte installiere Python 3 zuerst."
    exit 1
fi

# Virtuelle Umgebung erstellen, falls nicht vorhanden
if [ ! -d "cgm_env" ]; then
    echo "🔧 Erstelle virtuelle Umgebung..."
    $PYTHON -m venv cgm_env
    source cgm_env/bin/activate
    echo "📦 Installiere Abhängigkeiten..."
    pip install -r requirements.txt
else
    echo "✅ Virtuelle Umgebung gefunden."
    source cgm_env/bin/activate
fi

# Starte Streamlit App
echo "🚀 Starte CGMAnalyzer..."
streamlit run app/app.py
