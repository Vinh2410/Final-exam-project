from pre_processing import pre_process
from process import process_image

# Đường dẫn đến folder chứa ảnh gốc và folder output
input_folder = "./data/images"
hsv_folder = "./data/HSV_images"
output_folder = "./data/output_images"

if __name__ == "__main__":
    pre_process(input_folder, hsv_folder)
    
    process_image(hsv_folder, output_folder)