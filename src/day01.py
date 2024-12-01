lines: list[str] = read_lines("input/01")

result1 = 0
result2 = 0

l_list: list[int] = []
r_list: list[int] = []

for line in lines:
	parts = line.split()
	l_list.append(int(parts[0]))
	r_list.append(int(parts[1]))

l_list.sort()
r_list.sort()

for i in range(len(l_list)):
	result1 += abs(l_list[i] - r_list[i])

for item in l_list:
	result2 += item * r_list.count(item)

print("Part 1:", result1)
print("Part 2:", result2)
