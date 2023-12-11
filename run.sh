#!/bin/bash

VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating venv..."
    python3 -m venv $VENV_DIR
fi

source $VENV_DIR/bin/activate

if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing requirements..."
    pip install -r $REQUIREMENTS_FILE
else
    echo "Not found requirements.txt file."
    exit 1
fi

python internet_checker.py