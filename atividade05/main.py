import numpy as np
import matplotlib.pyplot as plt
import cv2

filename = 'figs/1_cumulus_000698.jpg'
# Load image file and convert from color to RGB
original_image = cv2.imread(filename)
img = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB, 0)
# converts the MxNx3 image into a Kx3 matrix where K=MxN
vectorized = img.reshape((-1,3))
# convert the unit8 values to float
vectorized = np.float32(vectorized)
# color clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
attempts = 10
ret,label,center = cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
# Regenerate image
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))

# Plot images
figure_size = 15
plt.figure(figsize=(figure_size,figure_size))
plt.subplot(1,2,1),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(result_image)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])
#plt.show()
plt.savefig('cloud_segmented.png', bbox_inches='tight')