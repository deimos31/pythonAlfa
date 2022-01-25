class MoneyMachine:
    """coin_value es un diccionario que no cambia"""
    COIN_VALUES= {
        'quarter':0.25,
        'dime': 0.10,
        'nikles': 0.05,
        'pennies':0.01
    }

    SYMBOL = '$'

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f'Money{self.SYMBOL}{self.profit}')


    def process_coins(self):
        """returns de total calculated from coins inserted"""
        print('please insert the coins')
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f'How many {coin}')*self.COIN_VALUES[coin])
            
        return self.money_received

    def make_payment(self,cost):
        """return True if the payment is accepted, or False if is insufficient"""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - (cost,2))
            print(f'Here is {self.SYMBOL}{change}in change')
            self.profit += cost
            self.money_received = 0

            return True

        else :
            print("Sorry, thats not enough money. Money refunded")
            self.money_received = 0
            return False