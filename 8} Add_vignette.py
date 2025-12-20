import numpy as np
import cv2

class StudioPortraitConverter:
    def __init__(self):
        print("Placeholder StudioPortraitConverter initialized.")
        print("In a full implementation, this would set up MediaPipe Selfie Segmenter and download models.")

    def generate_segmentation_mask(self, image):
        print("Generating placeholder segmentation mask.")
        mask = np.ones((image.shape[0], image.shape[1]), dtype=np.float32)
        return mask

    def enhance_subject(self, image, mask):
        print("Applying subject enhancement.")
        mask_3_channel = cv2.cvtColor((mask * 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)
        mask_3_channel_float = mask_3_channel / 255.0

        smoothed_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

        enhanced_image = image.copy()
        enhanced_image = (smoothed_image * mask_3_channel_float + enhanced_image * (1 - mask_3_channel_float)).astype(np.uint8)

        print("Subtle eye and lip enhancements would be applied here in a full implementation.")

        return enhanced_image

    def apply_dynamic_bokeh(self, enhanced_subject_image, original_image, segmentation_mask):
        print("Applying dynamic bokeh effect.")

        blurred_background = cv2.GaussianBlur(original_image, (55, 55), 0)

        mask_3_channel = cv2.cvtColor((segmentation_mask * 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)
        mask_3_channel_float = mask_3_channel / 255.0

        inverse_mask_float = 1 - mask_3_channel_float

        bokeh_image = (enhanced_subject_image * mask_3_channel_float + \
                       blurred_background * inverse_mask_float).astype(np.uint8)

        return bokeh_image

    def apply_studio_color_grade(self, image):
        print("Applying studio color grading.")
        image_float = image.astype(np.float32) / 255.0

        brightness_factor = 0.05
        contrast_factor = 1.1

        image_float = image_float * contrast_factor + brightness_factor

        image_float[:,:,2] = image_float[:,:,2] * 1.05
        image_float[:,:,1] = image_float[:,:,1] * 0.98
        image_float[:,:,0] = image_float[:,:,0] * 1.03

        image_float = np.clip(image_float, 0.0, 1.0)

        color_graded_image = (image_float * 255).astype(np.uint8)

        return color_graded_image

    def add_vignette(self, image):
        print("Applying vignette effect.")
        rows, cols = image.shape[:2]

        # Create a horizontal gradient (darker at edges, brighter at center)
      
        kernel_x = cv2.getGaussianKernel(cols, cols / 3)
        kernel_y = cv2.getGaussianKernel(rows, rows / 3)

        kernel = kernel_y * kernel_x.T
        mask = kernel / np.linalg.norm(kernel)
      
        # Normalize mask to range [0.5, 1.0] for a softer vignette
      
        mask = (mask - np.min(mask)) / (np.max(mask) - np.min(mask))
        mask = 0.5 + mask * 0.5 # Scale to 0.5-1.0 range

        # Apply the mask to the image
        # Convert image to float for multiplication
      
        image_float = image.astype(np.float32) / 255.0
        vignette_image = np.copy(image_float)

        for i in range(3):                                         # Apply to each channel (BGR)
            vignette_image[:,:,i] = vignette_image[:,:,i] * mask

        # Convert back to 8-bit unsigned integer
      
        vignette_image = (vignette_image * 255).astype(np.uint8)

        return vignette_image

# Re-instantiate the StudioPortraitConverter class with the updated methods.

converter = StudioPortraitConverter()
print("StudioPortraitConverter re-initialized with vignette method.")

# Apply vignette effect

vignette_image = converter.add_vignette(color_graded_image)

print("Vignette effect applied successfully.")
print(f"Shape of vignette_image: {vignette_image.shape}")
