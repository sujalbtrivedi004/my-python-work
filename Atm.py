class atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input= input("""1 for pin
                            2 for deposite
                            3 for enter 3 to withraw
                            4 check balace
                            5 exit""")
        if user_input == "1":
            print("create pin")
        elif user_input == "2":
            print("deposit")
        elif user_input == "3":
            print("withraw")
        elif user_input == "4":
            print("check balance")
        else:
            print("bye")
obj = atm()

