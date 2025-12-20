import cv2

# 1. Convert BGR to Lab color space

lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)

# 2. Split the Lab image into its L, a, and b channels

l_channel, a_channel, b_channel = cv2.split(lab_image)

# 3. Initialize a CLAHE object

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 4. Apply CLAHE to the L channel

clahe_l_channel = clahe.apply(l_channel)

# 5. Merge the enhanced L channel back with the original 'a' and 'b' channels

merged_lab_image = cv2.merge([clahe_l_channel, a_channel, b_channel])

# 6. Convert the merged Lab image back to the BGR color space

corrected_image = cv2.cvtColor(merged_lab_image, cv2.COLOR_LAB2BGR)

# 8. Print a confirmation message and display the shape

print("Lighting correction applied successfully using CLAHE.")
print(f"Shape of corrected_image: {corrected_image.shape}")
