lines: list[str] = read_lines("input/03")

result1 = 0

for line in lines:
	matches: list[str] = re_find_all("mul\\([0-9]+,[0-9]+\\)", line)
	for match in matches:
		nums = [int(num) for num in match[match.index("(") + 1:match.index(")")].split(",")]
		result1 += nums[0] * nums[1]

print("Part 1:", result1)
