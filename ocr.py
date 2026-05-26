# Import libraries
import cv2
import pytesseract
from PIL import Image

# For Windows users only
# Uncomment and set your Tesseract path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image_path = "sample.jpg"

# Read image using OpenCV
img = cv2.imread(image_path)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save temporary grayscale image
cv2.imwrite("temp.png", gray)

# Open image with PIL
temp_image = Image.open("temp.png")

# Extract text using OCR
text = pytesseract.image_to_string(temp_image)

# Display extracted text
print("Extracted Text:")
print(text)