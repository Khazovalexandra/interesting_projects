from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

Image.open(r'interesting_projects\Генерация картинок\images\garden on an exoplanet.jpg')
image = mpimg.imread(r'interesting_projects\Генерация картинок\images\garden on an exoplanet.jpg')
w, h, d = tuple(image.shape)
pix = np.reshape(image, (w*h, d))
n_colors = 10
model = KMeans(n_clusters=n_colors, random_state=42).fit(pix)
palette = np.uint8(model.cluster_centers_)
#plt.figure()
f, axarr = plt.subplots(1,2)
axarr[0].imshow(image)
axarr[1].imshow([palette])
plt.show()