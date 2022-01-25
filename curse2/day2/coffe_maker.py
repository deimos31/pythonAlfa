class CoffeMaker :
    '''Models the machine that makes coffee'''
    def __init__(self):
        self.resources={'water':400,'milk':400,'coffee':400}


    def report(self):
        '''Prints a report of all resources'''
        print(f'water: {self.resources["water"]}ml')
        print(f'milk: {self.resources["milk"]}ml')
        print(f'coffee: {self.resources["coffee"]}gr')




    def is_resources_sufficient(self,drink):
        """returns True when order could be made, False if ingredients are insufficient"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
             can_make = False
        return can_make

    def make_coffee(self,order):
        ''''''
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
            print(f'Here is your {order.name}. Enjoy it')





