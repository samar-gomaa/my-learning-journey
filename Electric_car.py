class car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def derive(self):
        print("driving the car")
    def show_info(self):
        print(f"the name of the car is {self.name} and the brand is {self.brand}")

class Battery:
    def __init__(self,battery_capacity:float=75):
        self.battery_capacity=battery_capacity


    def charge(self):
        print("Battery is charging ")   
    def check_range(self,current_charge):
        
        estimated_range=current_charge*5.0 # فرضا كل 1% بيدى 5 كيلو 
        print(f"current charge: {current_charge}%\nesimated remaining range: {estimated_range} Km")


class ElectricCar(car,Battery):
    def __init__(self, name, brand,battery_capacity:float=75):
        car.__init__(self,name,brand)
        Battery.__init__(self,battery_capacity)

mycar=ElectricCar(name="model 3",brand="tesla")    
mycar.show_info()
mycar.derive()
mycar.charge()
mycar.check_range(current_charge=80)    