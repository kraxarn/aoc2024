lines: list[str] = read_lines("input/05")

page_orders: list[list[int]] = []

result1 = 0
result2 = 0


def is_valid(update: list[int]) -> bool:
	for order in page_orders:
		if (set(order) & set(update)) != set(order):
			continue
		if update.index(order[0]) > update.index(order[1]):
			return False
	return True


def swap(items: list[int], item1: int, item2: int) -> None:
	items[item1], items[item2] = items[item2], items[item1]


def make_valid(update: list[int]) -> bool:
	for order in page_orders:
		if (set(order) & set(update)) != set(order):
			continue
		if update.index(order[0]) > update.index(order[1]):
			swap(update, update.index(order[0]), update.index(order[1]))
			return True
	return False


for line in lines:
	if "|" in line:
		page_orders.append([int(idx) for idx in line.split("|")])
	elif "," in line:
		nums = [int(idx) for idx in line.split(",")]
		if is_valid(nums):
			result1 += nums[len(nums) // 2]
		else:
			while make_valid(nums):
				pass
			result2 += nums[len(nums) // 2]

print("Part 1:", result1)
print("Part 2:", result2)
