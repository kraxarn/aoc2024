import typing

lines: list[str] = read_lines("input/04")

grid: list[list[str]] = []

result1 = 0

for line in lines:
	grid.append([ch for ch in line])


def get_char(grid_x: int, grid_y: int) -> typing.Optional[str]:
	if grid_x < 0 or grid_y < 0:
		return None
	if grid_x >= len(grid[y]) or grid_y >= len(grid):
		return None
	return grid[grid_y][grid_x]


def find(char: str, orig_x: int, orig_y: int) -> typing.Generator[
	typing.Tuple[int, int], None, None
]:
	for curr_x in range(orig_x - 1, orig_x + 2):
		for curr_y in range(orig_y - 1, orig_y + 2):
			if get_char(curr_x, curr_y) == char:
				yield curr_x, curr_y


for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == "X":
			for m in find("M", x, y):
				dir_x = m[0] - x
				dir_y = m[1] - y
				if get_char(m[0] + (dir_x * 1), m[1] + (dir_y * 1)) != "A":
					continue
				if get_char(m[0] + (dir_x * 2), m[1] + (dir_y * 2)) != "S":
					continue
				result1 += 1

print("Part 1:", result1)
#