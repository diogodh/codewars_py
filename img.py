import numpy as np
import scipy.misc as smp
from PIL import Image
import random
# Create a 1024x1024x3 array of 8 bit unsigned integers
# data = np.zeros( (1024,1024,3), dtype=np.uint8 )
# data[512,512] = [254,0,0]       # Makes the middle pixel red
# data[512,513] = [0,0,255]       # Makes the next pixel blue
# img.save('my.png')
i = 0
w, h = 1366, 768
data = np.zeros((h, w, 3), dtype=np.uint8)
k = int((w * h) / 2)
k2 = int(w * h)
w2 = w-1
h2 = h-1
k3 = random.randint(0, k2)

while i < k3:
    n = random.randint(0, w2)
    m = random.randint(0, h2)
    data[m:m+1, n:n+1] = [255, 255, 255]
    i += 1

img = Image.fromarray(data)
img.save('a.png')
# img.show()

left = random.randint(0, w2)
top = random.randint(0, h2)
right = random.randint(left, w)
bottom = random.randint(top, h)

print(left, top, right, bottom)

crop_rectangle = (left, top, right, bottom)
cropped_im = img.crop(crop_rectangle)
cropped_im.show()