import dataclasses
import enum
import typing

lines: list[str] = read_lines("input/06")

grid: list[list[str]] = []

result2 = 0


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


def load_grid():
	global grid
	grid = []
	for line in lines:
		grid.append([ch for ch in line])


def get_char(pos: Position) -> typing.Optional[str]:
	if pos.x < 0 or pos.y < 0:
		return None
	if pos.x >= len(grid[y]) or pos.y >= len(grid):
		return None
	return grid[pos.y][pos.x]


def turn(dir: Direction) -> Direction:
	if dir == Direction.UP:
		return Direction.RIGHT
	if dir == Direction.RIGHT:
		return Direction.DOWN
	if dir == Direction.DOWN:
		return Direction.LEFT
	if dir == Direction.LEFT:
		return Direction.UP


positions: list[Position] = []
directions: list[Direction] = []

load_grid()

for y in range(len(grid)):
	for x in range(len(grid[y])):
		position = Position(x, y)
		if get_char(position) == "^":
			positions.append(position)
			directions.append(Direction.UP)
			break

if len(positions) <= 0:
	raise "Starting point not found"


def walk() -> bool:
	while True:
		next_position = positions[-1].go(directions[-1])
		next_char = get_char(next_position)
		if next_char == "#":
			if directions[-1] == Direction.LEFT:
				directions.append(Direction.UP)
			else:
				directions.append(turn(directions[-1]))
			positions.append(positions[-1])
			continue
		if next_char == "." or next_char == "^":
			try:
				idx = positions.index(next_position)
				if directions[idx] == directions[-1]:
					return False
			except ValueError:
				pass
			positions.append(next_position)
			directions.append(directions[-1])
			continue
		if next_char is None:
			return True
		raise ValueError(next_char)


walk()

print("Part 1:", len(set(positions)))

for position in set(positions[1:]):
	load_grid()
	positions = positions[:1]
	directions = directions[:1]
	grid[position.y][position.x] = "#"
	if not walk():
		result2 += 1

print("Part 2:", result2)
