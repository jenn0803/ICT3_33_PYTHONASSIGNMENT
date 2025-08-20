import pandas as pd
import numpy as np

# Car class
class Car:
    def __init__(self, brand, model, price, color, fuel_type, year):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.fuel_type = fuel_type
        self.year = year
        self.car_id = np.random.randint(1000, 9999)  # unique car ID

    def get_details(self):
        return {
            "Car ID": self.car_id,
            "Brand": self.brand,
            "Model": self.model,
            "Price": self.price,
            "Color": self.color,
            "Fuel Type": self.fuel_type,
            "Year": self.year
        }

# Showroom class
class Showroom:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f" Car {car.brand} {car.model} added successfully!")

    def view_cars(self):
        if not self.inventory:
            print(" No cars available in the showroom.")
        else:
            df = pd.DataFrame([car.get_details() for car in self.inventory])
            print("\nAvailable Cars in Showroom:\n", df)

    def display_car_details(self, car_id):
        for car in self.inventory:
            if car.car_id == car_id:
                print("\nCar Details:")
                for key, value in car.get_details().items():
                    print(f"{key}: {value}")
                return
        print("Car not found.")

    def sell_car(self, car_id):
        for car in self.inventory:
            if car.car_id == car_id:
                self.inventory.remove(car)
                print(f" Car {car.brand} {car.model} sold successfully!")
                return
        print("Car not found for selling.")

    def buy_car(self):
        try:
            brand = input("Enter Car Brand: ")
            model = input("Enter Car Model: ")
            price = float(input("Enter Price: "))
            color = input("Enter Color: ")
            fuel_type = input("Enter Fuel Type: ")
            year = int(input("Enter Year: "))

            new_car = Car(brand, model, price, color, fuel_type, year)
            self.add_car(new_car)

        except ValueError as e:
            print(" Invalid input! Please enter correct details.")
            print("Error:", e)

# Main Program
if __name__ == "__main__":
    showroom = Showroom()

    # Adding some initial cars
    showroom.add_car(Car("Toyota", "Camry", 30000, "White", "Petrol", 2022))
    showroom.add_car(Car("BMW", "X5", 75000, "Black", "Diesel", 2023))
    showroom.add_car(Car("Tesla", "Model S", 90000, "Red", "Electric", 2024))

    while True:
        print("\n--- Car Showroom Menu ---")
        print("1. View Available Cars")
        print("2. Display Car Details")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            showroom.view_cars()
        elif choice == "2":
            try:
                car_id = int(input("Enter Car ID: "))
                showroom.display_car_details(car_id)
            except ValueError:
                print(" Please enter a valid Car ID.")
        elif choice == "3":
            try:
                car_id = int(input("Enter Car ID to sell: "))
                showroom.sell_car(car_id)
            except ValueError:
                print("Please enter a valid Car ID.")
        elif choice == "4":
            showroom.buy_car()
        elif choice == "5":
            print(" Exiting Car Showroom. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter between 1-5.")
