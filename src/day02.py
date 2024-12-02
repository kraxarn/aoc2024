lines: list[str] = read_lines("input/02")

result1 = 0
result2 = 0


def is_increasing(report: list[int]) -> int:
	for i in range(len(report) - 1):
		if report[i] >= report[i + 1]:
			return i
	return -1


def is_decreasing(report: list[int]) -> int:
	for i in range(len(report) - 1):
		if report[i] <= report[i + 1]:
			return i
	return -1


def is_adjacent(report: list[int]) -> int:
	for i in range(len(report) - 1):
		diff = abs(report[i + 1] - report[i])
		if diff < 1 or diff > 3:
			return i
	return -1


def is_safe(report: list[int]) -> int:
	idx_inc = is_increasing(report)
	idx_dec = is_decreasing(report)
	if idx_inc >= 0 and idx_dec >= 0:
		return max(idx_inc, idx_dec)
	return is_adjacent(report)


for line in lines:
	levels = [int(level) for level in line.split()]
	idx_unsafe = is_safe(levels)
	if idx_unsafe < 0:
		result1 += 1
		result2 += 1
	else:
		for i in range(idx_unsafe - 1, idx_unsafe + 2):
			temp = levels.copy()
			temp.pop(i)
			if is_safe(temp) < 0:
				result2 += 1
				break

print("Part 1:", result1)
print("Part 2:", result2)
