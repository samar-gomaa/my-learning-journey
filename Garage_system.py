class Garage:
    def __init__(self,total_cap:int):
        self.__total_cap=total_cap
        self.__available_spots=total_cap
        self.__registered_cars= []
        self.__parked_cars= []
    def add_car(self,car_id:str):
        if car_id not in self.__registered_cars:
            self.__registered_cars.append(car_id)
            print(f"car{car_id} registered in the system")
        else:
            print(f"car {car_id} is already registered")
        
    def remove_car(self,car_id:str):
        if car_id in self.__parked_cars:
            self.__parked_cars.remove(car_id)
            self.__available_spots+=1
            print(f"car {car_id}  removed successfully")
        else:
            print(f"car {car_id} is not in the garage")
    def park_car(self,car_id):
        if self.__available_spots<=0:
            print("the Garage is full,you can't park")
        elif car_id in self.__parked_cars:
            print(f"car {car_id} is already parked")
        else:
            self.__parked_cars.append(car_id)
            self.__available_spots-=1
            print(f"car {car_id} is now parked")
    def display_available_spot(self):
        print(f"availabe spots is : {self.__available_spots}")
            
my_garage=Garage(3)
my_garage.display_available_spot()
my_garage.park_car("ABC")  
my_garage.park_car("XYZ")                     
my_garage.display_available_spot()
my_garage.remove_car("ABC")
my_garage.display_available_spot()
        
