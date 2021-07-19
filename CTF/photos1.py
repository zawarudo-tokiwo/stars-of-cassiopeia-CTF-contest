from PIL import Image
import numpy as np

img = Image.open('/home/zawarudo/Downloads/13.png')
img = img.load()
d = [5, 11, 53, 55, 127, 265, 583, 635, 1397, 2915, 6731, 6985, 33655, 74041]
def get_image(w, h, img):
    w, h = 400, 1000
    data = np.zeros((w, h, 3), dtype=np.uint8)
    data[0:w, 0:h] = [255, 255, 255]

    x, y = 0, -1

    for i in range(173, 370378):
        x = i % w
        if x == 0:
            y += 1
        data[x, y] = img[i, 0]

    img = Image.fromarray(data, 'RGB')
    # img.save('my.png')
    img.show()
for i in d:
    get_image(i, 370205//i, img)













