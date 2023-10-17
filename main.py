from parking_lot import ParkingLot, Car

def main():
    try:
        # Input the total square footage size of the parking lot
        parking_lot_size = int(input("Enter the total square footage size of the parking lot: "))
        if parking_lot_size <= 0:
            raise ValueError("Square footage must be a positive number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Default spot size
    spot_size = (8, 12)

    # Check if the user wants to change the spot dimension
    change_spot_size = input(f"Do you want to change the spot dimension from {spot_size} (Y/N)? ").strip().lower()

    if change_spot_size == "y":
        try:
            # Input the new spot length and width in feet
            spot_length = int(input("Enter the new spot length in feet: "))
            spot_width = int(input("Enter the new spot width in feet: "))
            spot_size = (spot_length, spot_width)
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

    # Initialize the ParkingLot
    parking_lot = ParkingLot(parking_lot_size, spot_size)
    print(f"Total parking spots: {parking_lot.total_spots}")

    cars = []  # List to store Car instances

    while True:
        print("Choose an option:")
        print("1. Park a single car")
        print("2. Park multiple cars")
        print("3. Unpark a car")
        print("4. Unpark multiple cars")
        print("5. Save to JSON and Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Input a single license plate
            license_plate = input("Enter the license plate: ")
            car = Car(license_plate)
            park_choice = input("Do you want to park at a specific location? (Y/N): ").strip().lower()

            if park_choice == "y":
                spot_num = int(input("Enter the spot number: "))
                result = car.park(parking_lot, spot_num)
            else:
                result = car.park(parking_lot)

            print(result)
            cars.append(car)
        elif choice == "2":
            # Input a list of license plates as a comma-separated string
            input_license_plates = input("Enter a list of license plates (comma-separated): ")
            license_plates = [plate.strip() for plate in input_license_plates.split(',')]

            for plate in license_plates:
                # Check the validity of each license plate
                if len(plate) <= 7:
                    car = Car(plate)
                    result = car.park(parking_lot)
                    print(result)
                    cars.append(car)
                else:
                    print(f"License plate {plate} is improper and was not parked.")

        elif choice == "3":
            # Unpark a car
            license_plate = input("Enter the license plate of the car to unpark: ")
            unparked = False
            for car in cars:
                if car.license_plate == license_plate:
                    result = car.unpark(parking_lot)
                    print(result)
                    cars.remove(car)
                    unparked = True
                    break
            if not unparked:
                print(f"Car with license plate {license_plate} was not found in the parking lot.")
        elif choice == "4":
            # Unpark multiple cars
            input_license_plates = input("Enter a list of license plates to unpark (comma-separated): ")
            license_plates = [plate.strip() for plate in input_license_plates.split(',')]
            for license_plate in license_plates:
                unparked = False
                for car in cars:
                    if car.license_plate == license_plate:
                        result = car.unpark(parking_lot)
                        print(result)
                        cars.remove(car)
                        unparked = True
                        break
                if not unparked:
                    print(f"Car with license plate {license_plate} was not found in the parking lot.")
        elif choice == "5":
            # Save the parking lot state to a JSON file and exit
            filename = "parking_state.json"
            parking_lot.save_parking_lot_state(filename)
            print(f"Parking lot state has been saved to {filename}")
            break
        else:
            print(
                "Invalid choice. Please enter 1 to park a single car, 2 to park multiple cars, 3 to unpark a car, 4 to unpark multiple cars, or 5 to save to JSON and exit.")

    empty_spots = parking_lot.count_empty_spots()
    print(f"Number of empty spots: {empty_spots}")

if __name__ == "__main__":
    main()
