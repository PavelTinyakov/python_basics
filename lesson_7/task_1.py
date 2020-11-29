# Pavel Tinyakov

class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        result = ''
        for row in self.array:
            for el in row:
                result += f'{el}\t'
            result += '\n'
        return result

    def __add__(self, other):
        result = []
        for i in range(len(self.array)):
            row = []
            for j in range(len(self.array[i])):
                row.append(self.array[i][j] + other.array[i][j])
            result.append(row)
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [10, 11, 12]])
m3 = Matrix([[13, 14, 15], [16, 17, 18]])

print(m1 + m2 + m3)
