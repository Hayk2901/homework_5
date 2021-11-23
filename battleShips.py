q = False
x_count = 0
count = 0
matrix = input()
new_matrix = []
k = -1
for i in range(len(matrix)):
    if matrix[i] == '[':
        k += 1
matrix = matrix.replace('[', '')
matrix = matrix.replace(']', '')
matrix = matrix.replace('"', '')

l_m = matrix.split(',')

N = len(l_m)
for i in range(k):
    new_matrix.append([])
    for j in range(N//k):
        new_matrix[i].append(l_m[i*(N//k)+j])
# print(new_matrix)
for i in range(k):
    for j in range(N//k):
        if new_matrix[i][j] == 'X':
            x_count += 1
            if j-1 >= 0:
                if new_matrix[i][j-1] == 'X':
                    if j != N//k-1:
                        if new_matrix[i][j+1] == '.':
                            count += 1
                            q = False
                            continue
                    else:
                        count += 1
                        q = False
                        continue
                else:
                    if j == N//k-1:
                        count += 1
                        q = False
                        continue
                    else:
                        if new_matrix[i][j+1] == '.':
                            count += 1
                        q = True
                        continue
            else:
                if j == N//k-1:
                    count += 1
                    q = False
                    continue
                else:
                    if new_matrix[i][j + 1] == '.':
                        count += 1
                        q = False
                        continue
                    q = True

for j in range(N//k):
    for i in range(k):
        if new_matrix[i][j] == 'X':
            if i-1 >= 0:
                if new_matrix[i-1][j] == 'X':
                    if i != k-1:
                        if new_matrix[i+1][j] == '.':
                            count += 1
                            q = False
                            continue
                    else:
                        count += 1
                        q = False
                        continue
                else:
                    if i == k-1:
                        count += 1
                        q = False
                        continue
                    else:
                        if new_matrix[i+1][j] == '.':
                            count += 1
                        q = True
                        continue
            else:
                if i == k-1:
                    count += 1
                    q = False
                    continue
                else:
                    if new_matrix[i+1][j] == '.':
                        count += 1
                        q = False
                        continue
                    q = True
print(count-x_count)
