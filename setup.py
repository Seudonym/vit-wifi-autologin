import re
import os
print("This setup script will only run once, store your credentials in a .env file for the login script to access, and then delete itself.")
print(f"If you have somehow entered wrong credentials or would like to change the default credentials, you will have to modify the .env file located at ~/vit-wifi-autologin/.env yourself.\n")

userId = input("Enter registration number: ")
while not re.match(r'[0-9]{2}[A-Z]{3}[0-9]*', userId):
    userId = input("Enter a valid registration number: ")

passwd = input("\nEnter your password: ")
repasswd = input("Reenter your password: ")
while not passwd == repasswd or passwd == "":
    print("Passwords do not match. Try again.")
    passwd = input("\nEnter your password: ")
    repasswd = input("Reenter your password: ")

file = open(os.path.expanduser('~') + "\\vit-wifi-autologin\\.env", 'w')
file.write(f"USER_ID={userId}\nPASSWD={passwd}")
file.close()

print(r"Credentials saved. You can now login instantly with Win+R and then typing 'wifi'")
