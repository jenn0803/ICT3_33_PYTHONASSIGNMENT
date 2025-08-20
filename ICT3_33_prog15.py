import pandas as pd
import numpy as np

class Car:
    def __init__(self, brand ,model,price,color,fuel_type, year):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.fuel_type = fuel_type
        self.year = year
        self.car_id = np.random.randint(1000, 9999)
        
    def get_details(self):
        return {
            "Car Id" : self.car_id,
            "Brand" : self.brand,
            "Model": self.model,
            "Price": self.price,
            "Color": self.color,
            "Fuel-Type": self.fuel_type,
            "Year": self.year 
        }
    
class Showroom:
    def __init__(self):
        self.inventory =[]
        
    def add_car(self, car):
        self.inventory.append(car)
        print(f"Car {car.brand} {car.model} added successfully !")
        
    def view_cars(self):
        if not self.inventory:
            print("No car available in the showroom.")
        else:
            df= pd.DataFrame([car.get_details()for car in self.inventory])
            print("\nAvailable Cras in ShowRoom:\n",df)
    def display_car_details(self, car_id):
        for car in self.inventory:
            if car.car_id == car_id:
                print("\nCar Details:")
                for key, value in car.get_details().items():
                    print(f"{key}: {value}")
                return
        print("Car not found")
            
    def sell_car(self, car_id):
        for car in self.inventory:
            if car.car_id == car_id:
                self.inventory.remove(car)
                print(f"Car {car.brand} {car.model} sold succesfully")
                return
        print("Car not found for selling")
            
    def buy_car(self):
        try:
            brand = input("Enter your brand")
            model = input("Enter your Model")
            price = input("Enter your Price")
            color = input("Enter your Color")
            fuel_type = input("Enter your Fuel type")
            year = input("Enter your Year")
            
            new_car = Car(brand,model,price,color,fuel_type,year)
            self.add_car(new_car)
            
        except ValueError as e:
            print("Invail input Please Put Valid Values")
            print("Error", e)
            
if __name__ == "__main__":
    showroom = Showroom()
    
    showroom.add_car(Car("Toyota", "Camry", 30000, "White", "Petrol", 2022))
    showroom.add_car(Car("BMW", "X5", 75000, "Black", "Diesel", 2023))
    showroom.add_car(Car("Tesla", "Model S", 90000, "Red", "Electric", 2024))
    
    while True:
        print("\n--Car Showroom Menu--")
        print("1.View Available Cars.")
        print("2.Display Car Details")
        print("3.Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")
        
        choice = input("Enter Choice:")
        
        if choice =="1":
            showroom.view_cars()
        elif choice =="2":
            try:
                car_id = int(input("Enter car id:"))
                showroom.display_car_details(car_id)
            except ValueError:
                print("Plas enter a valid Car id:")
        elif choice == "3":
            try:
                car_id = int(input("Enter Car Id that needs to be selled"))
                showroom.sell_car(car_id)
            except ValueError:
                print("Plas enter a valid Car id:")
        elif choice =="4":
            showroom.buy_car()
        elif choice == "5":
            print("Exiting...... Byee")
            break
        else:
            print("Please Select a Valid Choice between 1 to 5 ")