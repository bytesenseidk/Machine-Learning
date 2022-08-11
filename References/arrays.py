import numpy as np

# Scalars
dim_0 = np.array(42)

# UNI-Dimentional Array
dim_1 = np.array([1, 2, 3, 4, 5])

# 2-Dimentional Array
dim_2 = np.array([[1, 2, 3],
                  [4, 5, 6]])

# 3-Dimentional Array
dim_3 = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[1, 2, 3], [4, 5, 6]]])

# x-dementional Array
dim_x = np.array([1, 2, 3, 4], ndmin=5)

# Check amount of dinemtions
check_dim = lambda fun: print(fun.ndim)
check_dim(dim_3)        # 3

print(dim_2)            # [[1 2 3]
                        # [4 5 6]]
print(dim_2.shape)      # (2, 3)
print(dim_2.size)       # 6
print(dim_2.ndim)       # 2
print(dim_2.data)       # <memory at 0x00000176CD503450>
print(np.append(dim_1[0], 99))
print(np.delete(dim_1[0], 1))