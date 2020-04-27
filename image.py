import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Picture:
    def __init__(self, path):
        self.path = path
    def display(self, seconds):
        ImageAddress = self.path
        ImageItself = Image.open(ImageAddress)
        ImageNumpyFormat = np.asarray(ImageItself)
        plt.imshow(ImageNumpyFormat)
        plt.draw()
        plt.pause(seconds)
        plt.close()
