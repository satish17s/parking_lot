import random
import string

def generate_random_license_plates(num_plates, plate_length=7):
    # Generate random license plates with the specified number and length
    plates = []
    characters = string.ascii_uppercase + string.digits  # Define characters for license plates
    for _ in range(num_plates):
        plate = ''.join(random.choice(characters) for _ in range(plate_length))  # Create a random license plate
        plates.append(plate)  # Add the generated license plate to the list
    return plates  # Return the list of generated license plates

if __name__ == "__main__":
    num_plates = int(input("Enter the number of random license plates to generate: "))
    generated_plates = generate_random_license_plates(num_plates)  # Generate random license plates
    print("Generated License Plates:")
    for plate in generated_plates:
        print(plate, end=",")  # Print the generated license plates with a comma separator
