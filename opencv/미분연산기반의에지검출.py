import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("/Users/bagseonghyeon/Desktop/schoolstudy/opencv/images/img16.jpg", cv2.IMREAD_GRAYSCALE)

res = [] 
img1_blur = cv2.GaussianBlur(img1, (3,3), 0)
res1 = cv2.Sobel(img1, cv2.FILTER_SCHARR, 1, 0, ksize=3)
res2 = cv2.Scharr(img1_blur, cv2.CV_32FC1, 0, 1)
res3 = cv2.Laplacian(img1_blur, cv2.CV_32FC1)

res4 = cv2.Canny(img1, 50, 200, apertureSize=5, L2gradient=True)

res.append(img1_blur), res.append(res1), res.append(res2), res.append(res3), res.append(res4)

titles = ["input", "soble(dx=1)", "sobel(dy=1)", "Laplacian", "Canny"]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(res[i], cmap='gray')
    plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])
    
plt.show()