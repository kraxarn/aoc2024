lines: list[str] = read_lines("input/02")

result1 = 0


def is_increasing(report: list[int]) -> bool:
	for i in range(len(report) - 1):
		if report[i] >= report[i + 1]:
			return False
	return True


def is_decreasing(report: list[int]) -> bool:
	for i in range(len(report) - 1):
		if report[i] <= report[i + 1]:
			return False
	return True


def is_adjacent(report: list[int]) -> bool:
	for i in range(len(report) - 1):
		diff = abs(report[i + 1] - report[i])
		if diff < 1 or diff > 3:
			return False
	return True


def is_safe(report: list[int]) -> bool:
	if not is_increasing(report) and not is_decreasing(report):
		return False
	if not is_adjacent(report):
		return False
	return True


for line in lines:
	levels = [int(level) for level in line.split()]
	if is_safe(levels):
		result1 += 1

print("Part 1:", result1)
