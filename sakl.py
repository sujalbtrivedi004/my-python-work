import getpass
import sys
import time

def display_password_on_enter():
    print("Type your Gmail password and press Enter to see it:")
    password = getpass.getpass()

    print("\nYou pressed Enter! Here's your password:")
    print(password)
    print("Press Enter again to exit...")
    input()

if __name__ == "__main__":
    display_password_on_enter()