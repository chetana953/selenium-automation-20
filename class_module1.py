class ABC:
    def __init__(self,car_name,car_company,car_price):
        self.name=car_name
        self.company=car_company
        self.price=car_price

    def get_car_price(self):
        return self.price
    def get_company_name(self):
        return self.company
    def get_car_name(self):
        return self.name
obj=ABC('Audi6', 'audi','30lac')
print(ABC.__name__)
print(ABC.__module__)
print(obj1.__module__)
