from array import array


class Matrix(object):

    def __init__(self, matrix: array):
        self.matrix = matrix
        
    def __add__(self, other):

        result = []
        if(len(self.matrix) == len(other.matrix)):
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[i])):
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])
        
            return Matrix(result)
        else:
            return None
    
    def __sub__(self, other):
        result = []
        if(len(self.matrix) == len(other.matrix)):
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[i])):
                    result[i].append(self.matrix[i][j] - other.matrix[i][j])
        
            return Matrix(result)
        else:
            return None

    def __mul__(self, other):
        result = []
        if(len(self.matrix[0]) == len(other.matrix)):

            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(other.matrix[0])):
                    result[i].append(0)
        
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(result)
        else:
            return None
    
    def __str__(self) -> str:
        return str(self.matrix)

    def get_matrix(self):
        return self.matrix