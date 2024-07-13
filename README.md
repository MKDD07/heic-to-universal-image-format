Sure, here's a more attractive and detailed README for your GitHub repository:

---

# HEIC to Universal Image Format Converter

The **HEIC to Universal Image Format Converter** is a Python-based tool designed to convert HEIC (High Efficiency Image Coding) files to various widely-used image formats such as PNG, JPG, BMP, and TIFF. This tool ensures compatibility across different platforms and applications that may not support the HEIC format natively.

## Features

- **Multi-format Support**: Convert HEIC files to PNG, JPG, BMP, and TIFF formats.
- **Batch Conversion**: Convert multiple HEIC files in a directory with a single command.
- **User-friendly Interface**: Simple and intuitive interface for selecting directories and formats.
- **Automated Directory Handling**: Automatically handles input and output directories, ensuring a smooth workflow.

## Requirements

To run this tool locally, you need to have the following Python packages installed:

```sh
pip install pyheif Pillow
```

For Google Colab, you can install the required packages using:

```sh
!pip install pyheif Pillow
!pip install ipywidgets
```

## Usage

### Local Usage

1. **Clone the repository**:
   ```sh
   git clone https://github.com/MKDD07/heic-to-universal-image-format.git
   cd heic-to-universal-image-format
   ```

2. **Install the required dependencies**:
   ```sh
   pip install pyheif Pillow
   ```

3. **Run the script**:
   ```sh
   python heic_converter.py
   ```

4. **Follow the prompts**:
   - Select the input directory containing HEIC files.
   - Select the output directory to save converted files.
   - Choose the desired output format (PNG, JPG, BMP, TIFF).

### Google Colab Usage

1. **Mount Google Drive**:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **Copy `main_gc.py` script to your Colab environment**.

3. **Install the required dependencies**:
   ```sh
   !pip install pyheif Pillow
   !pip install ipywidgets
   ```

4. **Run the `main_gc.py` script** in your Colab environment:
   ```python
   %run main_gc.py
   ```

## Example Script

### Local Python Script (`main.py`)

```python
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
```

## Contributing

We welcome contributions to enhance the functionality of this tool. Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
