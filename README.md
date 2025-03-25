# Rasengan Email

Rasengan Email is a Python-based email automation tool that allows you to send multiple emails with attachments and embedded images. It uses the `yagmail` library for seamless email delivery and includes logging for tracking sent emails.


## Features

- Send emails to multiple recipients.
- Choose from predefined email modes (100, 50, 25 emails) or set a custom count.
- Attach files and embed images in the email body.
- Logs all sent emails to `email_log.txt`.
- Supports Gmail, Yahoo, and Outlook SMTP servers.

## Prerequisites

Before using Rasengan Email, ensure you have the following installed:

1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **Required Libraries**: Install the required Python libraries using pip:
   ```bash
   pip install yagmail colorama art

## clone the repository
git clone https://github.com/caleb-elie/RasenganEmail.git
cd RasenganEmail

## clone the script
python rasengan_email.py

## For those facing problems in Kali try this:
# 1. Install venv if it's not installed
sudo apt install python3-venv  

# 2. Create a virtual environment
python3 -m venv venv  

# 3. Activate the virtual environment
source venv/bin/activate  

# 4. Install colorama inside the virtual environment
pip install colorama
pip install art
pip install yagmail

# 5. Check if it's installed
pip show colorama 
pip show art
pip show yagmail

