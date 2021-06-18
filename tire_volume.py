import math
from datetime import datetime

width = float( input( "Enter the width of the tire in mm (ex 205): " ) )
ratio = float( input( "Enter the aspect ratio of the tire (ex 60): " ) )
diameter = float( input( "Enter the diameter of the wheel in inches (ex 15): " ) )

volume = ((math.pi * (width ** 2.0) * ratio) * ((width * ratio) + (2540.0 * diameter)))/(10000000.0)
ounces = volume / 29.574

print(f"The approximate volume is {volume:.1f} milliliters ({ounces:.1f} ounces)")

purchase = input("Would you like to purchase tires with these dimensions(Yes or No)? ")

if purchase.lower() == "yes":
    phone = input("Please enter your phone number so we can help complete your purchase: ")

    current = str(datetime.now())
    split = current.split(" ", 1)
    date = split[0]

    with open("volumes.txt", "at") as volumes_file:

        # Print a car's model and dimensions to the file.
        print(f"{date}, {int(width)}, {int(ratio)}, {int(diameter)}, {volume:.1f}, {phone}", file=volumes_file)

elif purchase.lower() == "no":
    current = str(datetime.now())
    split = current.split(" ", 1)
    date = split[0]

    with open("volumes.txt", "at") as volumes_file:

        # Print a car's model and dimensions to the file.
        print(f"{date}, {int(width)}, {int(ratio)}, {int(diameter)}, {volume:.1f}", file=volumes_file)