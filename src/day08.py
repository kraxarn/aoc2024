import dataclasses
import typing

lines: list[str] = read_lines("input/08")

grid: list[list[str]] = []


@dataclasses.dataclass
class Position:
	x: int
	y: int

	def __hash__(self) -> int:
		return hash((self.x, self.y))

	def __add__(self, other: "Position") -> "Position":
		return Position(self.x + other.x, self.y + other.y)

	def __sub__(self, other: "Position") -> "Position":
		return Position(self.x - other.x, self.y - other.y)


for line in lines:
	grid.append([ch for ch in line])


def get_char(pos: Position) -> typing.Optional[str]:
	if pos.x < 0 or pos.y < 0:
		return None
	if pos.x >= len(grid[y]) or pos.y >= len(grid):
		return None
	return grid[pos.y][pos.x]


antennas: dict[str, list[Position]] = {}
anti_nodes: set[Position] = set()

for y in range(len(grid)):
	for x in range(len(grid[y])):
		position = Position(x, y)
		char = get_char(position)
		if char == ".":
			continue
		if char not in antennas:
			antennas[char] = []
		antennas[char].append(position)

for current_frequency, current_positions in antennas.items():
	for current_position in current_positions:
		for target_position in antennas[current_frequency]:
			if current_position == target_position:
				continue
			node_position = target_position + (target_position - current_position)
			if get_char(node_position) is None:
				continue
			anti_nodes.add(node_position)

print("Part 1:", len(anti_nodes))
anti_nodes.clear()

for current_frequency, current_positions in antennas.items():
	for current_position in current_positions:
		for target_position in antennas[current_frequency]:
			if current_position == target_position:
				continue
			diff = target_position - current_position
			node_position = target_position
			while get_char(node_position) is not None:
				anti_nodes.add(node_position)
				node_position += diff

print("Part 2:", len(anti_nodes))
