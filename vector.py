import math

class Vector_Algebra(object):
    def addition(self, vector_1, vector_2):
        result = []
        for index, num in enumerate(vector_1):
            result.append(num + vector_2[index])
        return result
    
    def subtraction(self, vector_1, vector_2):
        result = []
        for index, num in enumerate(vector_1):
            result.append(num - vector_2[index])
        return result
    
    def scalar_multiplication(self, vector, scalar):
        scaled_vector = []
        for num in vector:
            scaled_vector.append(num * scalar)
        return scaled_vector

    def magnitude(self, vector):
        """ Length of a vector, denoted as: ||v|| """
        vector_sum = 0
        for num in vector:
            vector_sum += pow(num, 2)
        return math.sqrt(vector_sum)


    def inner_product(self, vector_1, vector_2):
        """ Transpose or dot product """
        total = 0
        for index, num in enumerate(vector_1):
            total += (num * vector_2[index])
        return total


    def triangle_inequality(self, vector_1, vector_2):
        """the magnitude of the sum of vectors is always less than 
        or equal to the sum of the magnitudes of the vectors:
        ||v + u|| <= ||v|| + ||u|| 
        """
        vector_sum = self.addition(vector_1, vector_2)
        vector_1_mag = self.magnitude(vector_1)
        vector_2_mag = self.magnitude(vector_2)

        mag_of_sum = self.magnitude(vector_sum)    
        sum_of_mag = vector_1_mag + vector_2_mag
        return  mag_of_sum <= sum_of_mag
        

    def angle(self, vector_1, vector_2):
        transpose = self.inner_product(vector_1, vector_2)
        mag_1 = self.magnitude(vector_1)
        mag_2 = self.magnitude(vector_2)
        mag = mag_1 * mag_2
        return math.degrees(math.acos(transpose / mag))


    def arithmetic_mean(self, x, y):
        return (x + y) / 2

    def geometric_mean(self, x, y):
        return math.sqrt(x * y)


if __name__ == "__main__":
    vector = Vector_Algebra()
    vector_1, vector_2 = [7,9,4,3], [9,8,7,6]

    print(f"""Vectors: {vector_1}, {vector_2}
    Addition: {vector.addition(vector_1, vector_2)}
    Subtraction: {vector.subtraction(vector_1, vector_2)}
    Scalar Multiplication: {vector.scalar_multiplication(vector_1, 3)}
    Magnitude: {vector.magnitude(vector_1)}
    Transpose: {vector.inner_product(vector_1, vector_2)}
    Triangle of inequality: {vector.triangle_inequality(vector_1, vector_2)}
    Angle: {vector.angle([2,6], [-1, 5])}
    """)

