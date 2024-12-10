import dataclasses
import enum
import typing

lines: list[str] = read_lines("input/10")

grid: list[list[int]] = []

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
	grid.append([int(ch) for ch in line])


def get_height(pos: Position) -> typing.Optional[int]:
	if pos.x < 0 or pos.y < 0:
		return None
	if pos.y >= len(grid) or pos.x >= len(grid[pos.y]):
		return None
	return grid[pos.y][pos.x]


def get_heads(pos: Position) -> set[Position]:
	height = get_height(pos)
	if height == 9:
		return {pos}
	result: set[Position] = set()
	for direction in [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]:
		target_position = pos.go(direction)
		if get_height(target_position) == height + 1:
			result |= get_heads(target_position)
	return result


for y in range(len(grid)):
	for x in range(len(grid[y])):
		position = Position(x, y)
		if get_height(position) != 0:
			continue
		result1 += len(get_heads(position))

print("Part 1:", result1)
