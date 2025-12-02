import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create two black images
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw a white rectangle on first image
cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)

# Draw a white circle on second image
cv2.circle(img2, (150, 150), 100, 255, -1)

# Perform bitwise operations
bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

# Display all results
plt.figure(figsize=(10, 8))

plt.subplot(2, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title('Rectangle')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title('Circle')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(bitwise_and, cmap='gray')
plt.title('Bitwise AND')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(bitwise_or, cmap='gray')
plt.title('Bitwise OR')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(bitwise_xor, cmap='gray')
plt.title('Bitwise XOR')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(bitwise_not, cmap='gray')
plt.title('Bitwise NOT (Rectangle)')
plt.axis('off')

plt.tight_layout()
plt.show()

