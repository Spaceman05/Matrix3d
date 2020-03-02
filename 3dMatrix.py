class Matrix:
    def __init__(self, m, n):
        self.values = [[0]*m]*n

    def __str__(self):
        string = ""
        for i in self.values:
            string += "["
            for j in i:
                string += (str(j) + "\t")
            string += "]\n"
        return string

class MatricesOfDifferentOrder(Exception):
    """This operation can only occur on matrices of the same dimension and order"""

class Matrix3:
    def __init__(self, m, n, o):
        self.values = [[[0 for k in range(o)] for j in range(n)] for i in range(m)]

        self.m = m
        self.n = n
        self.o = o

    def __str__(self):
        string = ""
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                string += ("\t" * i * self.o) + "["
                for k in range(len(self.values[i][j])):
                    string += (str(self.values[i][j][k]) + "\t")
                string += "]\n"
        return string

    def __add__(self, other):
        if self.m is not other.m or self.n is not other.n or self.o is not other.o:
            raise MatricesOfDifferentOrder
            
        output = Matrix3(self.m, self.n, self.o)
        for i in range(self.m):
            for j in range(self.n):
                for k in range(self.o):
                    output.values[i][j][k] = self.values[i][j][k] + other.values[i][j][k]

        return output

    def __sub__(self, other):
        if self.m is not other.m or self.n is not other.n or self.o is not other.o:
            raise MatricesOfDifferentOrder
            
        output = Matrix3(self.m, self.n, self.o)
        for i in range(self.m):
            for j in range(self.n):
                for k in range(self.o):
                    output.values[i][j][k] = self.values[i][j][k] - other.values[i][j][k]

        return output

    def __iadd__(self, other):
        if self.m is not other.m or self.n is not other.n or self.o is not other.o:
            raise MatricesOfDifferentOrder
            
        for i in range(self.m):
            for j in range(self.n):
                for k in range(self.o):
                    self.values[i][j][k] = self.values[i][j][k] + other.values[i][j][k]

        return self
        
    def __getitem__(self, indices):
        return self.values[indices[0]][indices[1]][indices[2]]

    def __setitem__(self, indices, value):
        self.values[indices[0]][indices[1]][indices[2]] = value

    def det(self):
        if (self.m, self.n, self.o) == (2, 2, 2):
            return self[0, 0, 0] * self[1, 1, 1] + self[0, 1, 1] * self[1, 0, 0] - self[0, 1, 0] * self[1, 0, 1] - self[0, 0, 1] * self[1, 1, 0] 

A = Matrix3(2, 2, 2)
A.values = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

B = Matrix3(2, 2, 2)
B.values = [[[1, 5], [3, 7]], [[2, 6], [4, 8]]]
