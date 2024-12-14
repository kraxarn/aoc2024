import dataclasses
import typing

lines: list[str] = read_lines("input/13")

result1 = 0


@dataclasses.dataclass
class Position:
	x: int
	y: int


@dataclasses.dataclass
class Machine:
	button_a: Position
	button_b: Position
	prize: Position


machines: list[Machine] = []


def parse_position(line: str, sep: str) -> Position:
	x = line[line.find("X" + sep) + 1 + len(sep):line.find(", ")]
	y = line[line.find("Y" + sep) + 1 + len(sep):]
	return Position(int(x), int(y))


for i in range(0, len(lines), 4):
	machines.append(Machine(
		button_a=parse_position(lines[i + 0], "+"),
		button_b=parse_position(lines[i + 1], "+"),
		prize=parse_position(lines[i + 2], "="),
	))

for machine in machines:
	cost: typing.Optional[int] = None
	for a in range(100):
		for b in range(100):
			if machine.button_a.x * a + machine.button_b.x * b == machine.prize.x:
				if machine.button_a.y * a + machine.button_b.y * b == machine.prize.y:
					if cost is None:
						cost = 3 * a + b
					else:
						cost = min(cost, 3 * a + b)
	if cost is not None:
		result1 += cost

print("Part 1:", result1)
