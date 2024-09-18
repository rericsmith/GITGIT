# Raspberry Pi Smart Assistant

This repository contains the code and setup instructions to run a Python-based smart assistant on a Raspberry Pi.

## Setup Instructions

Follow these steps to install and run the smart assistant on your Raspberry Pi.

### 1. Clone the Repository

Open a terminal on your Raspberry Pi and run the following command to clone the repository:

```bash
git clone https://github.com/chandlerfarmer/Raspberry-Pi-Smart-Assistant.git
```
### 2. Navigate to the Project Directory
``` bash
cd Raspberry-Pi-Smart-Assistant
```
### 3. Check if Python is installed
By default most Debian-based systems have Python installed. Run the command to ensure it's installed:
```bash
python3 --version
```
The command will output the installed version of Python 3 if it is installed. If Python is not installed, it will return an error saying that the command is not found. If Python is installed go to step 4. If not installed then execute the commands below:
```bash
sudo apt update
sudo apt install python3
```
### 4. Run the Setup Script
The setup.sh script installs all necessary system dependencies and Python packages. Make sure the script is executable and then run it.
```bash
chmod +x setup.sh
./setup.sh
```
### 5. Configure Environment Variables
The assistant uses a .env file to store environment variables such as the users name, the assistants name, OpenAI API key, and the conversation size. 
```bash
nano .env
```
In the snippet below the assistant would be named Jarvis and Jarvis would address the user as John. Also, the conversation would reset after five messages.
```bash
NAME=John
ASSISTANT_NAME=Jarvis
OPEN_AI_KEY=your-openai-api-key
CONVERSATION_SIZE=5
```
After configuring the environment variables please save and exit the nano editor. 

### 6. Test the Assistant
Run the command below. Try engaging with the assistant. If the assistant is working as desired then proceed to the next step if you'd like to create a systemd service so that the assistant is always on!
```bash
python assistant.py
```
### 7. Install the Assistant as a Service
Make sure the install_service.sh script is executable:
```bash
chmod +x instasll_service.sh
```
Run the script with root priviledges:
```bash
sudo ./install_service.sh
```
### System Commands
To verify if the service is running correctly:
```bash
systemctl status raspberry_pi_smart_assistant.service
```
To Restart the Service:
```bash
sudo systemctl restart raspberry_pi_smart_assistant.service
```
If you make changes to the assistant code or pull updates from the repository, restart the service to apply the changes:
```bash
sudo systemctl restart raspberry_pi_smart_assistant.service
```
To Delete the Service: 
```bash
sudo systemctl stop raspberry_pi_smart_assistant.service
```
```bash
sudo rm /etc/systemd/system/raspberry_pi_smart_assistant.service
```
