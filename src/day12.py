import dataclasses
import enum

lines: list[str] = read_lines("input/12")

grid: list[list[str]] = []

result1 = 0


class Direction(enum.Enum):
	NONE = 0
	UP = 1
	RIGHT = 2
	DOWN = 3
	LEFT = 4


@dataclasses.dataclass
class Position:
	x: int
	y: int

	def go(self, target_dir: Direction) -> "Position":
		if target_dir == Direction.UP:
			return Position(self.x, self.y - 1)
		elif target_dir == Direction.RIGHT:
			return Position(self.x + 1, self.y)
		elif target_dir == Direction.DOWN:
			return Position(self.x, self.y + 1)
		elif target_dir == Direction.LEFT:
			return Position(self.x - 1, self.y)
		else:
			raise ValueError

	def __hash__(self) -> int:
		return hash((self.x, self.y))


for line in lines:
	grid.append([ch for ch in line])


def get_char(pos: Position) -> typing.Optional[str]:
	if pos.x < 0 or pos.y < 0:
		return None
	if pos.x >= len(grid[y]) or pos.y >= len(grid):
		return None
	return grid[pos.y][pos.x]


positions: set[Position] = set()


def get_region(plant: str, pos: Position) -> set[Position]:
	if pos in positions:
		return set()
	positions.add(pos)
	region_pos: set[Position] = {pos}
	for direction in [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]:
		target = pos.go(direction)
		if get_char(target) == plant:
			region_pos |= get_region(plant, target)
	return region_pos


def get_perimeter(plant: str, region_pos: set[Position]) -> int:
	value = 0
	for pos in region_pos:
		for direction in [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]:
			target_plant = get_char(pos.go(direction))
			if target_plant != plant:
				value += 1
	return value


regions: list[set[Position]] = []

for y in range(len(grid)):
	for x in range(len(grid)):
		position = Position(x, y)
		region = get_region(get_char(position), position)
		if len(region) <= 0:
			continue
		regions.append(region)

for region in regions:
	plant_type = get_char(list(region)[0])
	area = len(region)
	perimeter = get_perimeter(plant_type, region)
	result1 += (area * perimeter)

print("Part 1:", result1)
