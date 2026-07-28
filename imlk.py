import getpass

def display_password_on_enter():
    print("Type your password (it will be hidden):")
    
    # Hidden password input
    password = getpass.getpass()

    print("\nYou pressed Enter!")
    print("Your entered password is:")
    print(password)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    display_password_on_enter()
