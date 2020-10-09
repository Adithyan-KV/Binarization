import histograms
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def main():
    with Image.open("city.jpg") as image:
        image_data = np.asarray(image, dtype=np.uint8)
        luma_image_data = convert_to_greyscale(image_data)
        # luma_image = Image.fromarray(np.uint8(luma_image_data))
        # luma_image.show()
        # histograms.greyscale_histogram(image)
        # histograms.color_histogram(image)
        # binarized_data = binarize(luma_image_data, 50)
        # binary_image = Image.fromarray(np.uint8(binarized_data))
        # binary_image.show()
        threshold = get_optimum_threshold(luma_image_data)
        print(threshold)
        binarized_image_data = binarize(luma_image_data, threshold)
        binarized_image = Image.fromarray(np.uint8(binarized_image_data))
        binarized_image.show()
        binarized_image.save('output.jpg')


def get_optimum_threshold(image_data):
    threshold_with_max_var = 0
    max_variance = 0
    for threshold in range(255):
        print(threshold)
        c1 = []
        c2 = []
        for row in image_data:
            for pixel in row:
                if pixel > threshold:
                    c1.append(pixel)
                else:
                    c2.append(pixel)
        if not len(c1) == 0 and len(c2) == 0:
            w1 = len(c1) / np.size(image_data)
            w2 = len(c2) / np.size(image_data)
            interclass_variance = w1 * w2 * (np.mean(c1) - np.mean(c2))**2
            if interclass_variance > max_variance:
                threshold_with_max_var = threshold
                max_variance = interclass_variance
    return threshold_with_max_var


def convert_to_greyscale(image):
    weights_array = [0.30, 0.58, 0.12]
    image_matrix = np.matmul(image, weights_array)
    return image_matrix


def binarize(image_data, threshold):
    binarized_image_data = np.zeros_like(image_data)
    for row_index, row in enumerate(image_data):
        for column_index, pixel_value in enumerate(row):
            if pixel_value > threshold:
                binarized_image_data[row_index, column_index] = 255
    return binarized_image_data


if __name__ == "__main__":
    main()
