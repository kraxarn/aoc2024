lines: list[str] = read_lines("input/03")

result1 = 0
result2 = 0

def mul(value: str) -> int:
	nums = [int(num) for num in value[value.index("(") + 1:value.index(")")].split(",")]
	return nums[0] * nums[1]

for line in lines:
	matches: list[str] = re_find_all("mul\\([0-9]+,[0-9]+\\)", line)
	for match in matches:
		result1 += mul(match)

enabled = True

for line in lines:
	matches: list[str] = re_find_all("do\\(\\)|don't\\(\\)|mul\\([0-9]+,[0-9]+\\)", line)
	for match in matches:
		if match == "do()":
			enabled = True
		elif match == "don't()":
			enabled = False
		elif enabled:
			result2 += mul(match)

print("Part 1:", result1)
print("Part 2:", result2)
