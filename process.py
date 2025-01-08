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
            # Khử nhiễu với Gaussian Filter , phương sai bằng 1
            denoised_image = cv2.GaussianBlur(image, (3, 3), 1)

            # Khử nhiễu muối tiêu bằng medianBlur
            denoised_image_median = cv2.medianBlur(denoised_image, 3)

            # Làm sắc nét với Unsharp Mask
            blurred = cv2.GaussianBlur(image, (5, 5), 0)
            sharpened_image = cv2.addWeighted(
                denoised_image_median, 1.5, blurred, -0.5, 0
            )

            # Lưu ảnh
            cv2.imwrite(output_path, sharpened_image)
