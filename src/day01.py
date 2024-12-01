lines: list[str] = read_lines("input/01")

result1 = 0

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

print("Part 1:", result1)
