import enum
import typing

lines: list[str] = read_lines("input/07")

result1 = 0
result2 = 0


class Operation(enum.Enum):
	NONE = 0,
	PLUS = 1,
	MULT = 2,
	COMB = 3,

	def __repr__(self):
		if self == Operation.PLUS:
			return "+"
		if self == Operation.MULT:
			return "*"
		if self == Operation.COMB:
			return "||"
		return "?"


def get_combinations(length: int, operations: list[Operation], current: list[Operation]) -> typing.Generator[
	list[Operation], None, None
]:
	if len(current) == length:
		yield current
		return
	for operation in operations:
		for item in get_combinations(length, operations, current + [operation]):
			yield item


def merge(list1: list[int], list2: list[Operation]) -> typing.Generator[int | Operation, None, None]:
	for i1, item1 in enumerate(list1):
		yield item1
		if i1 < len(list2):
			yield list2[i1]


def calc(items: list[int | Operation]) -> int:
	for idx, item in enumerate(items):
		if item is Operation.PLUS:
			items[idx + 1] = items[idx - 1] + items[idx + 1]
		elif item is Operation.MULT:
			items[idx + 1] = items[idx - 1] * items[idx + 1]
		elif item is Operation.COMB:
			items[idx + 1] = int(str(items[idx - 1]) + str(items[idx + 1]))
	return items[-1]


for line in lines:
	parts = line.split(":")
	expected = int(parts[0])
	nums = [int(num) for num in parts[1].split()]
	for combination in get_combinations(len(nums) - 1, [Operation.PLUS, Operation.MULT], []):
		result = calc(list(merge(nums, combination)))
		if result == expected:
			result1 += result
			break
	for combination in get_combinations(len(nums) - 1, [Operation.PLUS, Operation.MULT, Operation.COMB], []):
		result = calc(list(merge(nums, combination)))
		if result == expected:
			result2 += result
			break

print("Part 1:", result1)
print("Part 2:", result2)
