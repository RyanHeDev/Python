from barcode import EAN13
from barcode.writer import ImageWriter
import os

# Create a folder for barcodes if it doesn't exist
output_folder = os.path.join("barcode generator", "barcodes")
os.makedirs(output_folder, exist_ok=True)

num_of_bar_codes = int(input("Enter how many barcodes do you want: "))

for i in range(num_of_bar_codes):
    id = input("Enter the 12 digit numbers for your barcode id: ")

    # Prompt the user for the barcode name
    name = input(f"Enter the name to save barcode {i + 1} (without extension): ")

    while not name:
        name = input("Please enter a valid name for the barcode (without extension): ")

    # Ensure the filename has the ".png" extension
    filename = os.path.join(output_folder, f"{name}.png" if not name.endswith(".png") else name)
    
    my_code = EAN13(id, writer=ImageWriter())
    my_code.save(filename)

    print(f"Barcode saved as {filename}")
