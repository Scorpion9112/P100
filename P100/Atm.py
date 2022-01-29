class Atm(object):
    def __init__(pinNumber, cardNumber):
        self.pinNumber=pinNumber
        self.cardNumber=cardNumber

    def withdraw(self):
        print("Insert card and enter pin number and card number then enter the amount you want to withdraw.")

    def balanceEnquiry(self):
        print("Insert card and enter pin number, once this is done the card number will appear with the amount of money remaining on the card.")

Crad= Atm("1234", "111-111-1111")
Card.withdraw()
Card.balanceEnquiry()