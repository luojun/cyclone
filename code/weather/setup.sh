#!/bin/bash

# Setup script for PanGu-Weather / EDA environment

echo "Setting up Python environment..."

# valid python version check could go here

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found."
    exit 1
fi

echo "Environment setup complete."
echo "To run the EDA agent loop: python3 eda/agent.py"
echo "To run the inference test: python3 weather/inference.py"
