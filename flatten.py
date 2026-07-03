
# .revel()-return a view :-original array will modify
# .flatten()-return a copy:-original not array will modify

import numpy as np

arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())