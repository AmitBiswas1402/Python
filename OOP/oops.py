class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
        
    def car_model_name(self):
        return f"{self.brand} {self.model}"
    
    def get_brand(self):
        return self.brand + " !"
    
    def fuel_type(self):
        return "Petrol"
    
    @staticmethod
    def gen_desc(self):
        return "Rich status"        
    
class EV(Car):
    def __init__(self, brand, model, battery_size) :
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
                
car1 = EV("Tesla", "Model Y", "85kWh")
car2 = Car("Lamborghini", "Huracan")

# print(isinstance(car1, Car))
# print(isinstance(car2, Car))

# print(car2.brand)
# print(car2.brand, car2.model)
# print(car2.fuel_type())
# print(car1.gen_desc())

# print(car1.brand)

# print(car1.brand, car1.model)
# print(car1.fuel_type())
# print(car1.total_car)

# print(car2.car_model_name())   

class Battery:
    def battery_info(self):
        return "Battery"
    
class Engine:
    def engine_info(self):
        return  "Engine"
    
class ElectriCar(Battery, Engine, Car):
    pass

newCar = ElectriCar("Mahindra", "Thar")
print(newCar.battery_info())
print(newCar.engine_info())