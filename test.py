from random import randint

from insane_coloured_triangles import triangle as triangle_new
from insane_coloured_triangles import iRGB_scheme


for k in range(100):
    rgb_list = [iRGB_scheme[randint(0, 2)] for i in range(randint(10000, 100000))]
    print(triangle_new(rgb_list))