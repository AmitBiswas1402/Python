class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def car_model_name(self):
        return f"{self.brand} {self.model}"
    
    def get_brand(self):
        return self.brand + " !"
    
class EV(Car):
    def __init__(self, brand, model, battery_size) :
        super().__init__(brand, model)
        self.battery_size = battery_size
                
car1 = EV("Tesla", "Model Y", "85kWh")
print(car1.brand)
print(car1.get_brand())
# print(car1.brand, car1.model)

# car2 = Car("Lamborghini", "Huracan")
# print(car2.brand, car2.model)

# print(car2.car_model_name())
        