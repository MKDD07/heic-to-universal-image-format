import os
import pyheif
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to convert HEIC to the selected format
def convert_heic(heic_file, output_file, output_format):
    heif_file = pyheif.read(heic_file)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(output_file, output_format.upper())

# Function to select directories
def select_directory(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory(title=prompt)
    if not directory:
        messagebox.showerror("Error", "You must select a directory!")
        raise ValueError("Directory selection cancelled")
    return directory

# Prompt user to select input and output directories
try:
    input_dir = select_directory("Select the input directory containing HEIC files")
    output_dir = select_directory("Select the output directory to save converted files")
except ValueError:
    exit()

# Prompt user for output format
format_options = ['PNG', 'JPG', 'BMP', 'TIFF']
print("Select the output format:")
for i, option in enumerate(format_options, 1):
    print(f"{i}. {option}")

format_choice = int(input("Enter the number corresponding to the desired format: "))
output_format = format_options[format_choice - 1]

# Convert each HEIC file in the input directory to the selected format
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.heic'):
        heic_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.' + output_format.lower()
        output_path = os.path.join(output_dir, output_filename)

        convert_heic(heic_path, output_path, output_format)
        print(f'Converted {heic_path} to {output_path}')

print("Conversion completed successfully!")
