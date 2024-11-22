import os
import numpy as np
import cv2


def pre_process(input_folder, output_folder):
    
    # Tạo folder output nếu chưa tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Duyệt qua tất cả ảnh trong folder input
    for filename in os.listdir(input_folder):
        if (
            filename.endswith(".jpg")
            or filename.endswith(".png")
            or filename.endswith(".jpeg")
        ):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            img = cv2.imread(input_path)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)

            # Khoảng giá trị HSV cho màu da (ví dụ)
            lower_skin = np.array([0, 20, 70])
            upper_skin = np.array([20, 255, 255])

            mask = cv2.inRange(hsv, lower_skin, upper_skin)

            # Loại bỏ nhiễu
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.dilate(mask, kernel, iterations=1)

            # Find contours
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                c = max(contours, key = cv2.contourArea)
                x, y, w, h = cv2.boundingRect(c)
                cropped_img = img[y:y+h, x:x+w]
                cv2.imwrite(output_path, cropped_img)
            else:
                print(f"No skin detected in {filename}")

