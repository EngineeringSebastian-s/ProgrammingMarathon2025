import numpy as np

vec_a = input().split(",")
vec_b = input().split(",")

data = []
line = input().split(",")
while line != ["0"]:
    data.append(line)
    line = input().split(",")

matrix = np.zeros((len(vec_a), len(vec_b)))

for i in range(len(data)):

    fill = data[i][0]
    col = data[i][1]

    if vec_a.count(fill) == 0 and vec_b.count(col) == 0:
        fill = data[i][1]
        col = data[i][0]

    pos_fill = vec_a.index(fill)
    pos_col = vec_b.index(col)
    matrix[pos_fill][pos_col] = 1

matrix_transpose = np.transpose(matrix)

is_simetric=True
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (matrix[i][j] != matrix_transpose[i][j]):
            is_simetric = False

if is_simetric:
    print("1")
else:
    print("2")