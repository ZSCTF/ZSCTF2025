import matplotlib.pyplot as plt
from base64 import b64decode
from os import listdir
import numpy as np

def tupper(k):
    def f(x, y):
        y += k
        a1 = 2**-(-17*x - y % 17)
        a2 = (y // 17) // a1
        return 0 if a2 % 2 > 0.5 else 1
    a = np.zeros((17, 106))
    for y in range(17):
        for x in range(106):
            a[y, x] = f(x, y)
    return a[::-1, :]

files = listdir("t4pper")
files.sort(key=lambda x: int(x.split(".")[0]))
source = ''
for file in files:
    with open(f"t4pper/{file}", "r") as f:
        source += f.read()

source = int(b64decode(source).decode())
image = tupper(source)
plt.imshow(image, cmap='gray')
plt.show()
