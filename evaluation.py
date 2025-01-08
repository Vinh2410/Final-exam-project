import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
import os


def calculate_psnr(img1, img2):
    """Calculates the Peak Signal-to-Noise Ratio (PSNR) between two images.

    Args:
        img1: The first image.
        img2: The second image.

    Returns:
        float: The PSNR value.
    """
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float("inf")
    return 20 * np.log10(255 / np.sqrt(mse))


def calculate_ssim(img1, img2):
    """Calculates the Structural Similarity Index (SSIM) between two images.

    Args:
        img1: The first image.
        img2: The second image.
        data_range: The window size for SSIM calculation.

    Returns:
        float: The SSIM value.
    """
    # Convert images to grayscale for SSIM calculation
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate SSIM
    ssim_value = ssim(gray1, gray2, data_range=255)
    return ssim_value


def evaluate_image(img1_folder, img2_folder, evaluate_txt):
    """Evaluates the PSNR and SSIM between images in two folders.

    Args:
        img1_folder: Path to the folder containing the first set of images.
        img2_folder: Path to the folder containing the second set of images.
    """
    with open(evaluate_txt, "w") as f:
        f.write("Filename\tPSNR\tSSIM\n")
        for filename in os.listdir(img1_folder):
            if (
                filename.endswith(".jpg")
                or filename.endswith(".png")
                or filename.endswith(".jpeg")
            ):
                img1_path = os.path.join(img1_folder, filename)
                img2_path = os.path.join(img2_folder, filename)

                try:
                    img1 = cv2.imread(img1_path)
                    img2 = cv2.imread(img2_path)

                    psnr = calculate_psnr(img1, img2)
                    ssim_value = calculate_ssim(img1, img2)

                    f.write(f"{filename}\t{psnr:.2f}\t{ssim_value:.4f}\n")

                except Exception as e:
                    f.write(f"Error processing {filename}: {e}\n")
