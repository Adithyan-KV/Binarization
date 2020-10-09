import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def main():
    print("something")


def greyscale_histogram(image):
    image_data = np.asarray(image)
    weights_array = [0.30, 0.58, 0.12]
    luma_image_data = np.matmul(image_data, weights_array)
    hist, bins = np.histogram(luma_image_data, bins=256)
    plt.bar(bins[:-1], hist, color='grey', width=1)
    plt.title("Image histogram")
    plt.xlabel("Luma Value")
    plt.ylabel("Number of pixels with luma value")
    plt.show()


def color_histogram(image):
    image_data = np.asarray(image)
    red_channel = image_data[:, :, 0]
    green_channel = image_data[:, :, 1]
    blue_channel = image_data[:, :, 2]
    r_hist, r_bins = np.histogram(red_channel, bins=256,)
    plt.bar(r_bins[:-1], r_hist, color='red', width=1, alpha=0.5)
    g_hist, g_bins = np.histogram(green_channel, bins=256)
    plt.bar(g_bins[:-1], g_hist, color='green', width=1, alpha=0.5)
    b_hist, b_bins = np.histogram(blue_channel, bins=256)
    plt.bar(b_bins[:-1], b_hist, color='blue', width=1, alpha=0.5)
    plt.xlabel("Color Values")
    plt.ylabel("Number of pixels with color values")
    plt.legend(['red', 'green', 'blue'])
    plt.show()


if __name__ == "__main__":
    main()
