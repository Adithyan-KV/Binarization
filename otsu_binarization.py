import histograms
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time


def main():
    with Image.open("test_images/bridge.jpg") as image:
        image_data = np.asarray(image, dtype=np.uint8)
        luma_image_data = convert_to_greyscale(image_data)
        # For visualizations
        # luma_image = Image.fromarray(np.uint8(luma_image_data))
        # luma_image.show()
        # luma_image.save('luma.png')
        # histograms.greyscale_histogram(image)
        # histograms.color_histogram(image)
        start = time.time()
        threshold = get_optimum_threshold(luma_image_data)
        end = time.time()
        print(threshold)
        runtime = end - start
        print(runtime)
        binarized_image_data = binarize(luma_image_data, threshold)
        binarized_image = Image.fromarray(np.uint8(binarized_image_data))
        # binarized_image.show()
        binarized_image.save('output.jpg')


def get_optimum_threshold(image_data):
    number_of_pixels = np.size(image_data)
    threshold_with_max_var = 0
    max_variance = 0
    variance_array = np.zeros(255)
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
        if len(c1) != 0 and len(c2) != 0:
            w1 = len(c1) / number_of_pixels
            w2 = len(c2) / number_of_pixels
            interclass_variance = w1 * w2 * (np.mean(c1) - np.mean(c2))**2
            if interclass_variance > max_variance:
                threshold_with_max_var = threshold
                max_variance = interclass_variance
            variance_array[threshold] = interclass_variance
    print(threshold_with_max_var)
    # plot_variance_curve(variance_array, max_variance)
    return threshold_with_max_var


def plot_variance_curve(variance_array, max_variance):
    threshold_array = np.arange(0, 255, 1)
    plt.plot(threshold_array, variance_array)
    plt.axvline(max_variance, color='black')
    plt.annotate(text='maxima', xy=(max(variance_array), max_variance + 40))
    plt.xlabel("threshold")
    plt.ylabel("interclass variance")
    plt.title("threshold vs variance")
    plt.show()


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
