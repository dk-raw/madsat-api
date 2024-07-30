#!/bin/bash
cd /home/nikolakis/madsat-api
echo "Pulling latest changes from GitHub..."
git pull origin main

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Restarting the application..."
sudo systemctl restart madsat-api.service
echo "Update complete!"