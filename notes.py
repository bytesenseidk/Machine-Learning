# Note Section
""" 
Eigenvalue: Ez
Eigenvector: Ex
__________________
- Example 1:
Ez:   Ex:
13 *  [3] == [39]
      [4]    [52]

- Example 2:
Ez:       Ex:
[ 1, 9] * [3] == [39]
[12, 4]   [4]    [52]
-------
[13, 13] = Eigenvalue(13)


The magnitude of the product of a scalar "k", and a vector "v", is 
equal to the absolute value of the scalar and the magnitude of the
origional vector: |k| * ||v||
sqrt(pow(k, 2)) = |k|
|k| = absolute value of the scalar
- the absolute value of a number is always positive
|-8|(11) = 8(11) = 88
"""

""" Matrix arithmetic """

amanda = [15, 10,  5,  9, 1]
betty  = [10,  9,  4,  9, 2]
clark  = [20,  0,  0, 23, 1]
dennis = [15,  6, 10,  6, 5]

pay = [110, 200, 600, 60, 100]

def total(person, payload):
    result = 0
    for index, amount in enumerate(person):
        result += payload[index] * amount
    return result

amanda_pay = total(amanda, pay)
betty_pay = total(betty, pay)
clark_pay = total(clark, pay)
dennis_pay = total(dennis, pay)

results = f"""
[ Total Payments ]:
Amanda: {amanda_pay}
Betty:  {betty_pay}
Clark:  {clark_pay}
Dennis: {dennis_pay}
"""


def vectorInMatrix(a, b):
    for i, j in zip(a, b):
        print(f"list_1: {i}\tlist_2: {j}")

def numInMatrix(a, b):
    for i, j in zip(a, b):
        for x, y in zip(i, j):
            print(f"list_1: {x}\tlist_2: {y}")

def addMatrices(a, b):
    for i, j in zip(a, b):
        for index, x, y in enumerate(zip(i, j)):
            a[i][index] = x + y
    return a


list_1 = [[1, 2, 3],[3, 2, 1],
          [1, 2, 3],[3, 2, 1]]

list_2 = [[4, 5, 6],[6, 5, 4],
          [4, 5, 6],[6, 5, 4]]


vectorInMatrix(list_1, list_2)
numInMatrix(list_1, list_2)

""" Matrix arithmetic
matrix multiplication:

    the number of columns in the first matrix must be the same as the number of rows in the second matrix.

    To perform matrix multiplication on m × n - matrix A and p × q - matrix B, 
    it is necessary that n = p. Furthermore, the resulting matrix A * B has dimension m × q.

    For example, if matrix A has dimension 3 × 4 and matrix B has dimension 4 × 7, 
    then the product A * B has dimension 3 × 7. But you can’t multiply the matrices in the reverse order. 
    The product B * A cannot be performed, because matrix B has seven columns and matrix A has three rows.

    if you’re finding the element a 23 in the product matrix A, you get that element by multiplying all the elements 
    in the second row of the first matrix times the elements in the third column of the second matrix and then adding up the products.


A = [[1, 2, 3]
     [1, 2, 3]
     [1, 2, 3]]

B = [[4, 5, 6]
     [4, 5, 6]
     [4, 5, 6]]

A * B = [[24, 30, 45]
         [24, 30, 45]
         [24, 30, 45]]


A = [[1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]]

B = [[9, 6, 3]
     [8, 5, 2]
     [7, 4, 1]]

A * B = [[ 46,  28, 10]
         [118,  73, 28]
         [190, 118, 46]]

a = 9 + 16 + 21
b = 6 + 10 + 12
c = 3 + 4 + 3

d = 36 + 40 + 42
e = 24 + 25 + 24
f = 12 + 10 + 6

g = 63 + 64 + 63
h = 42 + 40 + 36
i = 21 + 16 + 9

"""
# import numpy as np

# A = ([1, 2, 3],[4, 5, 6],[7, 8, 9])
# B = ([9, 6, 3],[8, 5, 2],[7, 4, 1])
# identity_matrix = ([1, 0, 0],[0, 1, 0],[0, 0, 1])

# print(np.dot(A, identity_matrix))