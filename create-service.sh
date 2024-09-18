#!/bin/bash

# Ensure the script is run as root
if [[ "$EUID" -ne 0 ]]; then 
  echo "Please run as root (use sudo)"
  exit 1
fi

# Get the username of the user who invoked sudo
if [[ -n "$SUDO_USER" ]]; then
  CURRENT_USER="$SUDO_USER"
else
  CURRENT_USER=$(whoami)
fi

SERVICE_NAME="raspberry_pi_smart_assistant"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

echo "Creating systemd service file at $SERVICE_FILE"

# Create the systemd service file
cat <<EOT > $SERVICE_FILE
[Unit]
Description=Assistant Service
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/venv/bin/python $(pwd)/assistant.py
Restart=always

[Install]
WantedBy=multi-user.target
EOT

echo "Reloading systemd daemon..."
systemctl daemon-reload

echo "Enabling $SERVICE_NAME service to start on boot..."
systemctl enable $SERVICE_NAME.service

echo "Starting $SERVICE_NAME service..."
systemctl start $SERVICE_NAME.service

echo "$SERVICE_NAME service installed and started successfully!"
