import typing

line: str = read_lines("input/09")[0]

disk_map: list[typing.Optional[int]] = []

result1 = 0


def swap(items: list, item1: int, item2: int) -> None:
	items[item1], items[item2] = items[item2], items[item1]


def is_good(items: list[typing.Optional[int]]) -> bool:
	none_idx = items.index(None)
	for item in items[:none_idx - 1]:
		if item is None:
			return False
	for item in items[none_idx + 1:]:
		if item is not None:
			return False
	return True


for i, digit in enumerate(line):
	for file in range(int(digit)):
		disk_map.append(i // 2 if i % 2 == 0 else None)

for i in reversed(range(len(disk_map))):
	if disk_map[i] is None:
		continue
	if is_good(disk_map):
		break
	swap(disk_map, i, disk_map.index(None))

for i, digit in enumerate(disk_map):
	if digit is None:
		break
	result1 += i * int(digit)

print("Part 1:", result1)
