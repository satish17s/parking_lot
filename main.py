from parking_lot import ParkingLot, Car

def main():
    try:
        parking_lot_size = int(input("Enter the total square footage size of the parking lot: "))
        if parking_lot_size <= 0:
            raise ValueError("Square footage must be a positive number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    spot_size = (8, 12)  # Default spot size

    change_spot_size = input(f"Do you want to change the spot dimension from {spot_size} (Y/N)? ").strip().lower()

    if change_spot_size == "y":
        try:
            spot_length = int(input("Enter the new spot length in feet: "))
            spot_width = int(input("Enter the new spot width in feet: "))
            spot_size = (spot_length, spot_width)
        except ValueError as e:
            print(f"Invalid input: {e}")
            return

    parking_lot = ParkingLot(parking_lot_size, spot_size)
    print(f"Total parking spots: {parking_lot.total_spots}")

    # Input a list of license plates as a comma-separated string
    input_license_plates = input("Enter a list of license plates (comma-separated): ")
    license_plates = [plate.strip() for plate in input_license_plates.split(',')]

    cars = [Car(plate) for plate in license_plates]

    for car in cars:
        result = car.park(parking_lot)
        print(result)

    parking_lot.save_parking_lot_state("parking_state.json")


if __name__ == "__main__":
    main()
