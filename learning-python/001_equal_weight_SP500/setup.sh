#!/bin/bash

# Create virtual environment
python3 -m venv .venv

# Activate the venv
source .venv/bin/activate

# Upgrade pip to latest version 
pip install --upgrade pip

# Install the dependencies from requirements.txt 
pip install -r requirements.txt
echo "Venv started and all dependencies installed"
