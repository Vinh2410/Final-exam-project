import cv2
import os
import numpy as np


def process_image(input_folder, output_folder):

    # Tạo folder nếu chưa có
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Duyệt qua tất cả ảnh
    for filename in os.listdir(input_folder):
        if (
            filename.endswith(".jpg")
            or filename.endswith(".png")
            or filename.endswith(".jpeg")
        ):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            image = cv2.imread(input_path)
            if image is None:
                print("Image not found")
                continue
            # Khử nhiễu với Gaussian Filter
            denoised_image = cv2.GaussianBlur(image, (3, 3), 1)

            # Làm sắc nét với Unsharp Mask
            sharp_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            sharpened_image = cv2.filter2D(denoised_image, -1, sharp_kernel)

            # Save the processed image
            cv2.imwrite(output_path, sharpened_image)
