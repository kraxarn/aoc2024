import dataclasses
import enum
import typing

lines: list[str] = read_lines("input/06")

grid: list[list[str]] = []


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
direction = Direction.NONE

for y in range(len(grid)):
	for x in range(len(grid[y])):
		position = Position(x, y)
		if get_char(position) == "^":
			positions.append(position)
			direction = Direction.UP
			break

if len(positions) <= 0:
	raise "Starting point not found"

while True:
	next_position = positions[-1].go(direction)
	next_char = get_char(next_position)
	if next_char == "#":
		if direction == Direction.LEFT:
			direction = Direction.UP
		else:
			direction = turn(direction)
		continue
	if next_char == "." or next_char == "^":
		positions.append(next_position)
		continue
	if next_char is None:
		break
	raise ValueError(next_char)

print("Part 1:", len(set(positions)))
