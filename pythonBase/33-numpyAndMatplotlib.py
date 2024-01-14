import numpy as np
import matplotlib.pyplot as mp

image = mp.imread("img.png")
print(image)
mp.imshow(image)

gray_value = np.array([0.299, 0.587, 0.114])
image2 = np.dot(image, gray_value)
mp.imshow(image2,cmap="gray")
mp.show()