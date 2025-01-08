from pre_processing import pre_process
from process import process_image

from evaluation import evaluate_image

# Đường dẫn đến folder chứa ảnh gốc và folder output
input_folder = "./data/images"
hsv_folder = "./data/HSV_images"
output_folder = "./data/output_images"

if __name__ == "__main__":
    pre_process(input_folder, hsv_folder)

    process_image(input_folder, output_folder)
    # Bước tiền xử lý làm ảnh hưởng nặng đến chất lượng ảnh đầu vào bộ lọc
    # print(evaluate_image(hsv_folder, output_folder))
    evaluate_image(input_folder, output_folder, "./evaluate/results.txt")
    evaluate_image(input_folder, input_folder, "./evaluate/results.txt")
