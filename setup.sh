#!/bin/bash

# Ensure the script is run as a non-root user
if [[ "$EUID" -eq 0 ]]; then 
  echo "Please do not run as root"
  exit 1
fi

# Update the system's package index
echo "Updating system..."
sudo apt update -y

# Install necessary system packages if not already installed
echo "Installing system dependencies..."
sudo apt install -y python3-pip python3-dev build-essential libasound2-dev portaudio19-dev

# Check if a virtual environment is active, if not, create one
if [[ -z "$VIRTUAL_ENV" ]]; then
  echo "No virtual environment detected. Creating one..."
  python3 -m venv venv
  echo "Virtual environment created. Activating the virtual environment..."
  source venv/bin/activate
else
  echo "Virtual environment is already active."
fi

# Ensure pip is up-to-date
echo "Upgrading pip..."
pip install --upgrade pip

# Install the required Python packages
echo "Installing Python dependencies..."
pip install speechrecognition pyttsx3 openai python-dotenv

echo "All dependencies installed successfully!"
