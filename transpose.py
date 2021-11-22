matrix = input()
new_matrix = []
k = 0
for i in range(len(matrix)):
    if matrix[i] == '[':
        k += 1
if k != 1:
    k -= 1
matrix = matrix.replace('[', '')
matrix = matrix.replace(']', '')
l_m = matrix.split(',')
for j in range(len(l_m)//k):
    new_matrix.append([])
    for i in range(j, len(l_m), len(l_m)//k):
        new_matrix[j].append(l_m[i])
print(new_matrix)
