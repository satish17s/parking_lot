import json


class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        self.spot_size = spot_size
        self.total_spots = square_footage // (spot_size[0] * spot_size[1])
        self.parking_spots = [None] * self.total_spots
        self.parked_cars = {}  # To keep track of parked cars

    def map_vehicles_to_parked_spots(self):
        mapping = {}
        for car_license_plate, spot_num in self.parked_cars.items():
            mapping[car_license_plate] = spot_num
        return mapping

    def save_parking_lot_state(self, filename):
        parking_state = self.map_vehicles_to_parked_spots()
        with open(filename, 'w') as file:
            json.dump(parking_state, file)

    def find_empty_spot(self):
        for spot_num, car in enumerate(self.parking_spots):
            if car is None:
                return spot_num
        return -1

    def park_car(self, car, spot_num):
        if 0 <= spot_num < self.total_spots and self.parking_spots[spot_num] is None:
            self.parking_spots[spot_num] = car
            return f"Car with license plate {car} parked successfully in spot {spot_num}"
        else:
            return f"Car with license plate {car} could not be parked in spot {spot_num}"


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.is_parked = False

    def __str__(self):
        return f"Car with license plate: {self.license_plate}"

    def park(self, parking_lot):
        if self.is_parked:
            return f"Car with license plate {self.license_plate} is already parked in spot {parking_lot.parked_cars[self.license_plate]}."

        # Check if the license plate is already in the set of parked cars
        if self.license_plate in parking_lot.parked_cars:
            return f"Car with license plate {self.license_plate} is already parked in spot {parking_lot.parked_cars[self.license_plate]}."

        spot_num = parking_lot.find_empty_spot()
        if spot_num != -1:
            result = parking_lot.park_car(self.license_plate, spot_num)
            if "successfully" in result:
                self.is_parked = True
                parking_lot.parked_cars[self.license_plate] = spot_num
            return result
        else:
            return f"Car with license plate {self.license_plate} could not find an empty spot."
