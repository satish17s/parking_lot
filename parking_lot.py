import json
import os


class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        # Initialize the ParkingLot with square footage and spot size
        self.spot_size = spot_size
        self.total_spots = square_footage // (spot_size[0] * spot_size[1])  # Calculate total parking spots
        self.parking_spots = [None] * self.total_spots  # Initialize parking spots as a list of None
        self.parked_cars = {}  # To keep track of parked cars

    def map_vehicles_to_parked_spots(self):
        # Create a mapping of vehicles to their parked spots as a dictionary
        mapping = {}
        for car_license_plate, spot_num in self.parked_cars.items():
            mapping[car_license_plate] = spot_num
        return mapping

    def save_parking_lot_state(self, filename):
        # Get the current working directory
        current_directory = os.getcwd()
        # Combine the current directory and the filename to get the full path
        file_path = os.path.join(current_directory, filename)

        parking_state = self.map_vehicles_to_parked_spots()
        with open(file_path, 'w') as file:
            json.dump(parking_state, file)

    def find_empty_spot(self):
        # Find an empty parking spot and return its spot number
        for spot_num, car in enumerate(self.parking_spots):
            if car is None:
                return spot_num
        return -1

    def park_car(self, car, spot_num):
        if 0 <= spot_num < self.total_spots and self.parking_spots[spot_num] is None:
            # Park a car in the specified spot
            self.parking_spots[spot_num] = car
            return f"Car with license plate {car} parked successfully in spot {spot_num}"
        else:
            return f"Car with license plate {car} could not be parked in spot {spot_num}"

    def unpark_car(self, car):
        if car.license_plate in self.parked_cars:
            spot_num = self.parked_cars[car.license_plate]
            self.parking_spots[spot_num] = None
            del self.parked_cars[car.license_plate]
            self.save_parking_lot_state("parking_state.json")
            car.is_parked = False
            return f"Car with license plate {car.license_plate} has been unparked from spot {spot_num}."
        else:
            return f"Car with license plate {car.license_plate} is not currently parked."

    def count_empty_spots(self):
        # Count the number of empty parking spots
        return sum(1 for spot in self.parking_spots if spot is None)

class Car:
    def __init__(self, license_plate):
        while len(license_plate) > 7:
            print("License plate should not exceed 7 characters.")
            license_plate = input("Enter a valid license plate: ")
        self.license_plate = license_plate
        self.is_parked = False

    def park(self, parking_lot, spot_num=None):
        if self.is_parked:
            return f"Car with license plate {self.license_plate} is already parked in spot {parking_lot.parked_cars[self.license_plate]}."

        # Check if the license plate is already in the set of parked cars
        if self.license_plate in parking_lot.parked_cars:
            return f"Car with license plate {self.license_plate} is already parked in spot {parking_lot.parked_cars[self.license_plate]}."

        if spot_num is not None:
            result = parking_lot.park_car(self.license_plate, spot_num)
        else:
            spot_num = parking_lot.find_empty_spot()
            if spot_num != -1:
                result = parking_lot.park_car(self.license_plate, spot_num)
            else:
                return f"Car with license plate {self.license_plate} could not find an empty spot."

        if "successfully" in result:
            self.is_parked = True
            parking_lot.parked_cars[self.license_plate] = spot_num
        return result

    def unpark(self, parking_lot):
        return parking_lot.unpark_car(self)
