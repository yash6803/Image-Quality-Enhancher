import cv2

# Define the output path for the enhanced image

output_path = "/content/output_portrait.jpg"

# Save the final enhanced image

cv2.imwrite(output_path, vignette_image)

print(f"Enhanced image saved successfully to {output_path}")
