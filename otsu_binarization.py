import histograms
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def main():
    with Image.open("image.jpg") as image:
        image_data = np.asarray(image, dtype=np.uint8)
        luma_image_data = convert_to_greyscale(image_data)
        luma_image = Image.fromarray(np.uint8(luma_image_data))
        # luma_image.show()
        histograms.greyscale_histogram(image)
        histograms.color_histogram(image)


def convert_to_greyscale(image):
    weights_array = [0.30, 0.58, 0.12]
    image_matrix = np.matmul(image, weights_array)
    return image_matrix


if __name__ == "__main__":
    main()
