import cv2
import numpy as np 

# -----STEP-1------
# Reading the image
# img_path = r'AI\1.ColorImgToBinary\ImgOfLordShiva.jpg'
img_path = r'AI\3.FacialRecognizer\test_img1.jpg'
# img_path = r'AI\Images\nature2.jpg'
img = cv2.imread(img_path)

#Resizing the image
#Interpolation is xubic for best results
img_resized = cv2.resize(img, None, fx=2.0, fy=2.0)

# -----STEP-2------
# Clearing Impurities
img_cleared = cv2.medianBlur(img_resized, 3)
img_cleared = cv2.medianBlur(img_cleared, 3)
img_cleared = cv2.medianBlur(img_cleared, 3) #did it thrice since for creating an art we need a very very filtered image
 
# Restores color variations i.e. makes colors constants =>low variations
img_cleared = cv2.edgePreservingFilter(img_cleared, sigma_s=2)


# -----STEP-3------
# Applying filtering
img_filtered = cv2.bilateralFilter(img_cleared, 3, 30, 30)

for i in range(2):
    img_filtered = cv2.bilateralFilter(img_filtered, 3, 20, 20)

for i in range(2):
    img_filtered = cv2.bilateralFilter(img_filtered, 3, 10, 10)

# for i in range(3):
#     img_filtered = cv2.bilateralFilter(img_filtered, 5, 40, 10)


# -----STEP-4------
# Tuning the Art
# We will have to do sharpen the img since blurred becoz of prev. step
gaussian_mask = cv2.GaussianBlur(img_filtered, (7,7), 30)
for i in range(5):
    img_sharp = cv2.addWeighted(img_filtered, 1.5, gaussian_mask, -0.5, 3)

# for i in range(2):
#     img_sharp = cv2.addWeighted(img_filtered, 2.0, gaussian_mask, -1.0, 0)



# -----STEP-5------
# Displaying the images with a larger window size
cv2.namedWindow("Final Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Img with Clear impurities", cv2.WINDOW_NORMAL)
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)

# Set the window sizes
cv2.resizeWindow("Final Image", 600, 400)
cv2.resizeWindow("Img with Clear impurities", 600, 400)
cv2.resizeWindow("Original Image", 600, 400)

# Displaying the images
cv2.imshow("Final Image", img_sharp)
cv2.imshow("Img with Clear impurities", img_cleared)
cv2.imshow("Original Image", img_resized)
cv2.waitKey(0)
