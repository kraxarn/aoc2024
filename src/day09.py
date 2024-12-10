import typing

line: str = read_lines("input/09")[0]

disk_map: list[typing.Optional[int]] = []

result1 = 0
result2 = 0


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

map_str = ""

for digit in disk_map:
	map_str += str(digit) if digit is not None else "."

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

for i in reversed(range(len(map_str))):
	if map_str[i - 1] == map_str[i]:
		continue
	if map_str[i] == ".":
		continue
	length = int(line[int(map_str[i]) * 2])
	target_idx = map_str.find("." * length)
	if target_idx < 0:
		continue
	if target_idx > i:
		continue
	data = map_str[i:i + length]
	map_str = map_str[:target_idx] + data + map_str[target_idx + length:]
	map_str = map_str[:i] + ("." * length) + map_str[i + length:]

for i, digit in enumerate(map_str):
	if digit == ".":
		continue
	result2 += i * int(digit)

print("Part 2:", result2)
