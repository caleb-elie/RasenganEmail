import sys
import time
import logging
import os
from getpass import getpass
from colorama import Fore, Style, init
from art import text2art
import yagmail  

init(autoreset=True)

logging.basicConfig(filename='email_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def banner():
    ascii_art = text2art("Rasengan Email", font="small")
    print(Fore.BLUE + ascii_art)
    print(Fore.BLUE + '+[+[+[ Ethical and Responsible use  ]+]+]+')
    print(Fore.BLUE + '+[+[+[ Author: C4l3bpy ]+]+]+')

class EmailRasengan:
    def __init__(self):
        try:
            print(Fore.WHITE + '\n+[+[+[ Initializing program... ]+]+]+' + Style.RESET_ALL)
            self.targets = input(Fore.GREEN + 'Enter target emails (comma-separated): ' + Style.RESET_ALL).split(',')
            self.mode = int(input(Fore.GREEN + 'Enter email mode (1:100, 2:50, 3:25, 4:custom): ' + Style.RESET_ALL))
            if self.mode not in [1, 2, 3, 4]:
                print(Fore.RED + 'ERROR: Invalid option. Exiting.' + Style.RESET_ALL)
                sys.exit(1)
        except Exception as e:
            print(Fore.RED + f'ERROR: {e}' + Style.RESET_ALL)
            sys.exit(1)

    def set_email_count(self):
        try:
            if self.mode == 1:
                self.amount = 100
            elif self.mode == 2:
                self.amount = 50
            elif self.mode == 3:
                self.amount = 25
            else:
                self.amount = int(input(Fore.GREEN + 'Enter custom email count: ' + Style.RESET_ALL))
            print(Fore.YELLOW + f'\n+[+[+[ Sending {self.amount} emails to {len(self.targets)} recipients ]+]+]+' + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f'ERROR: {e}' + Style.RESET_ALL)
            sys.exit(1)

    def configure_email(self):
        try:
            print(Fore.RED + '\n+[+[+[ Configuring email settings ]+]+]+' + Style.RESET_ALL)
            self.server = input(Fore.CYAN + 'Enter SMTP server (or choose 1:Gmail, 2:Yahoo, 3:Outlook): ' + Style.RESET_ALL)
            if self.server == '1':
                self.server = 'smtp.gmail.com'
                self.port = 465
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
                self.port = 465
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
                self.port = 465
            else:
                self.port = int(input(Fore.GREEN + 'Enter SMTP port (e.g., 465): ' + Style.RESET_ALL))

            self.fromAddr = input(Fore.MAGENTA + 'Enter your email address: ' + Style.RESET_ALL)
            self.fromPwd = getpass(Fore.MAGENTA + 'Enter your email password (or app password if 2FA is enabled): ' + Style.RESET_ALL)
            self.subject = input(Fore.MAGENTA + 'Enter email subject: ' + Style.RESET_ALL)
            
            print(Fore.MAGENTA + 'Enter email message (type END on a new line to finish): ' + Style.RESET_ALL)
            self.message = ""
            while True:
                line = input()
                if line == "END":
                    break
                self.message += line + "\n"

            self.attachments = input(Fore.MAGENTA + 'Enter file paths to attach (comma-separated, e.g., file1.pdf, image.png): ' + Style.RESET_ALL).split(',')
            self.attachments = [file.strip() for file in self.attachments if file.strip() and os.path.exists(file.strip())]

            self.images = input(Fore.MAGENTA + 'Enter image paths to embed in the message (comma-separated, e.g., image1.png, photo.jpg): ' + Style.RESET_ALL).split(',')
            self.images = [image.strip() for image in self.images if image.strip() and os.path.exists(image.strip())]

            missing_files = [file for file in self.attachments if not os.path.exists(file)]
            missing_images = [image for image in self.images if not os.path.exists(image)]

            if missing_files or missing_images:
                print(Fore.RED + f'ERROR: The following files or images do not exist: {missing_files + missing_images}' + Style.RESET_ALL)
                sys.exit(1)

        except Exception as e:
            print(Fore.RED + f'ERROR: {e}' + Style.RESET_ALL)
            sys.exit(1)

    def send_emails(self):
        try:
            print(Fore.RED + '\n+[+[+[ Sending emails... ]+]+]+' + Style.RESET_ALL)
            yag = yagmail.SMTP(self.fromAddr, self.fromPwd)

            for target in self.targets:
                for i in range(self.amount):
                    contents = [self.message]

                    for image in self.images:
                        contents.append(yagmail.inline(image))

                    contents.extend(self.attachments)

                    yag.send(to=target, subject=self.subject, contents=contents)
                    logging.info(f'Sent email to {target}')
                    print(Fore.CYAN + f'Sent email {i + 1} to {target}' + Style.RESET_ALL)
                    time.sleep(1)

            print(Fore.RED + '\n+[+[+[ Emails sent successfully! ]+]+]+' + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f'ERROR: {e}' + Style.RESET_ALL)
            logging.error(f'Error: {e}')

if __name__ == '__main__':
    banner()
    rasengan = EmailRasengan()
    rasengan.set_email_count()
    rasengan.configure_email()
    rasengan.send_emails()