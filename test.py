from PIL import Image
import base64
import io
import sys

# Check if the user provided a file path as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 base64-encoder.py <file path>")
    sys.exit(1)

# Get the image file path from the command-line argument
image_path = sys.argv[1]

try:
    # Load the image file
    image = Image.open(image_path)

    # Convert the image to a byte stream
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format='PNG')
    image_byte_array = image_byte_array.getvalue()

    # Encode the image byte array to base64
    base64_encoded = base64.b64encode(image_byte_array).decode()

    # Print the base64-encoded image
    print('data:image/png;base64,' + base64_encoded)
except Exception as e:
    print(f"Error: {str(e)}")