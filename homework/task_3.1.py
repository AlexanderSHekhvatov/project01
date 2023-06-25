class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None] * columns for _ in range(rows)]

    def set_value(self, row, column, value):
        if row < 1 or row > self.rows or column < 1 or column > self.columns:
            raise ValueError("Invalid row or column index")
        self.matrix[row - 1][column - 1] = value

    def get_value(self, row, column):
        if row < 1 or row > self.rows or column < 1 or column > self.columns:
            raise ValueError("Invalid row or column index")
        return self.matrix[row - 1][column - 1]

    def get_num_rows(self):
        return self.rows

    def get_num_columns(self):
        return self.columns

    def display(self):
        for row in self.matrix:
            print(row)


import random

matrix = []
for i in range(1, 11):
    row = []
    for j in range(2, 11):
        if j == 1:
            row.append(i)
        else:
            random_number = random.randint(1, 100)
            row.append(random_number)
    matrix.append(row)

for row in matrix:
    print(row)

