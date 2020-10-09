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
        # histograms.greyscale_histogram(image)
        # histograms.color_histogram(image)
        binarized_data = binarize(luma_image_data, 140)
        binary_image = Image.fromarray(np.uint8(binarized_data))
        binary_image.show()


def convert_to_greyscale(image):
    weights_array = [0.30, 0.58, 0.12]
    image_matrix = np.matmul(image, weights_array)
    return image_matrix


def binarize(image_data, threshhold):
    binarized_image_data = np.zeros_like(image_data)
    for row_index, row in enumerate(image_data):
        for column_index, pixel_value in enumerate(row):
            if pixel_value > threshhold:
                binarized_image_data[row_index, column_index] = 255
    return binarized_image_data


if __name__ == "__main__":
    main()
