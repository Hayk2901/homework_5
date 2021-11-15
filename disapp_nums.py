nums = input()
nums = nums.replace("[", "")
nums = nums.replace(']', '')
list_nums = nums.split(",")

output_list = []
set_nums = set()

n = len(list_nums)
for i in range(n):
    set_nums.add(int(list_nums[i]))
for i in range(1, n+1):
    if i not in set_nums:
        output_list.append(i)
print(output_list)
