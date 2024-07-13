import os
import pyheif
from PIL import Image
import ipywidgets as widgets
from IPython.display import display

# Define the input and output directories
input_dir = '/content/drive/My Drive/Images'
output_dir = '/content/drive/My Drive/output'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

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

# Dropdown widget for selecting the output format
format_dropdown = widgets.Dropdown(
    options=['PNG', 'JPG', 'BMP', 'TIFF'],
    value='PNG',
    description='Format:',
    disabled=False,
)

display(format_dropdown)

# Convert each HEIC file in the input directory to the selected format
def convert_images(b):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.' + format_dropdown.value.lower()
            output_path = os.path.join(output_dir, output_filename)

            convert_heic(heic_path, output_path, format_dropdown.value)
            print(f'Converted {heic_path} to {output_path}')

# Button to start conversion
convert_button = widgets.Button(
    description='Convert Images',
    disabled=False,
    button_style='',
    tooltip='Click to start conversion',
    icon='check'
)

convert_button.on_click(convert_images)
display(convert_button)
