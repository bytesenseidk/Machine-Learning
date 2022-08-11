class Matrix_Algebra(object):

    def addition(self, matrix_1, matrix_2):
        if len(matrix_1) != len(matrix_2):
            return "Matrices not the same dimension"
        else:
            result = [[matrix_1[row][col] + matrix_2[row][col] for col in range(len(matrix_1[0]))] for row in range(len(matrix_1))] 
            return result

    def subtraction(self, matrix_1, matrix_2):
        if len(matrix_1) != len(matrix_2):
            return "Matrices not the same dimension"
        else:
            result = [[matrix_1[row][col] - matrix_2[row][col] for col in range(len(matrix_1[0]))] for row in range(len(matrix_1))] 
            return result

    def scalar_multiplication(self, matrix, scalar):
        result = [[col * scalar for col in row] for row in matrix]
        return result


if __name__ == "__main__":
    matrix = Matrix_Algebra()
    matrix_1_2x2 = [[9, 8], [7, 6]]
    matrix_2_2x2 = [[5, 4], [3, 2]]
    
    matrix.addition(matrix_1_2x2, matrix_2_2x2)
    print(matrix.scalar_multiplication(matrix_1_2x2, 2))

    matrix_1_3x5 = [[1, 2, 3, 4, 5], 
                    [2, 3, 4, 5, 6], 
                    [3, 4, 5, 6, 7]]
    
    print(matrix.scalar_multiplication(matrix_1_3x5, 2))

    matrix_2_3x5 = matrix_1_3x5
