set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
k1, k2, k3 = 0, 0, 0
words = input()
words = words.replace("[", "")
words = words.replace("]", "")
words = words.replace('"', "")
list_words = words.split(",")
output_list = []
n = len(list_words)
for i in range(n):
    for j in range(len(list_words[i])):
        if list_words[i][j] in set1:
            k1 += 1
        if list_words[i][j] in set2:
            k2 += 1
        if list_words[i][j] in set3:
            k3 += 1
    if k1 + k2 == 0 or k1 + k3 == 0 or k3 + k2 == 0:
        output_list.append(list_words[i])
    k1, k2, k3 = 0, 0, 0
print(output_list)
