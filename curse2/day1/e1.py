#Waiter
class waiter:
    def __init__(self,name,age,weekend):
        #attributes
        self.name =name
        self.age = age
        self.gender = 'male'
        self.work_on_weekends = weekend

        self.introduce()
        self.menu()

    def introduce(self):
        print (f'Hello, my names es {self.name}')

    def menu(self):
        print('the menu today is...')

    def work_on_weekend(self):
        if self.work_on_weekends== True:
            print(f'{self.name} work on weekends')
        else:
            print(f'{self.name} doesnt work on weekends')    

        

waiter1 = waiter('Raul',20,True)
waiter1.work_on_weekend()
#waiter2 = waiter('Antonio',24,False)


