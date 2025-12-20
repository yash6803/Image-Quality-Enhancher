import cv2

### Define the input path for the image ###

input_path = "/content/sample_data/input.jpg"

### Load the image using cv2.imread() ###

input_image = cv2.imread(input_path)

### Check if the image was loaded successfully ###

if input_image is None:
    print(f"Error: Could not load image from {input_path}")
else:
    print(f"Image loaded successfully from {input_path}")
    print(f"Image shape: {input_image.shape}")
