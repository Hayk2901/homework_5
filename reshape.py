matrix = input()
matrix_copy = matrix
r = int(input())
n = int(input())

new_matrix = []

matrix = matrix.replace('[', '')
matrix = matrix.replace(']', '')
l_m = matrix.split(',')
N = len(l_m)
if len(l_m) != r * n:
    print(matrix_copy)
else:
    for i in range(r):
        new_matrix.append([])
        for j in range(i * n, (i+1) * n, 1):
            new_matrix[i].append(l_m[j])
    print(new_matrix)
