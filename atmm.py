
class Atm:
    #cunstructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hii how can i help you ? 
        1.Press 1 for create your pin :
        2.Press 2 for change your pin with the help of old pin :
        3.Press 3 for change your pin by forgeting
        4.Press 4 for check your balance :
        5.Press 5 withdraw your balance :
        6.Anything for exit :   """)

        if user_input == '1':
            self.create_pin()
            #create pin
        elif user_input == '2':
            self.change_pin()
            #change the pin
        elif user_input == '3':
            self.forget_pin()
        elif user_input == '4':
            self.balance_check()
            #balance
        elif user_input == '5':
            self.withdraw_balance()
        else:
            print('exit')

    def create_pin(self):
        self.pin = int(input('enter your pin but only 4 digit numeric:'))
        self.balance = int(input('enter your balance'))
        print('your pin successfully created')
        return self.menu()

    def change_pin(self):
        old_pin = int(input('enter your old pin: '))
        if old_pin == self.pin:
            self.pin = int(input('enter new pin:'))
            print('pin successfully updated')
        else:
            print('you have entered wrong pin please try again')
        self.menu()

    def balance_check(self):
        user_pin = int(input('Enter your pin '))
        if user_pin == self.pin:
            print('Your account balance is :', self.balance)
        else:
            print('You have entered wrong pin please try again ')
        self.menu()

    def withdraw_balance(self):
        pin = int(input('Enter the pin'))
        if pin == self.pin:
            balance = int(input('Enter the amount:'))
            if balance <= self.balance and balance > 0:
                self.balance = self.balance - balance
                print('Withdrawal successful')
                print('Your left amount is', self.balance)
            else:
                print('Your account does not have a sufficient balance')
        else:
            print('Please enter the right pin')
        self.menu()

    def forget_pin(self):
        balnce = int(input('Enter your current balance:'))
        if balnce == self.balance:
            new_pin = int(input('Enter the new pin'))
            self.pin = new_pin
            print('Your pin successfully changed')
        else:
            print('Enter the right amount otherwise you can not chaage the pin')
        self.menu()


obj = Atm()
