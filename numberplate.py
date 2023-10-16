import random
import string


def generate_random_license_plates(num_plates, plate_length=7):
    plates = []
    characters = string.ascii_uppercase + string.digits
    for _ in range(num_plates):
        plate = ''.join(random.choice(characters) for _ in range(plate_length))
        plates.append(plate)
    return plates



if __name__ == "__main__":
    num_plates = int(input("Enter the number of random license plates to generate: "))
    generated_plates = generate_random_license_plates(num_plates)
    print("Generated License Plates:")
    for plate in generated_plates:
        print(plate, end=",")
