import dataclasses

lines: list[str] = read_lines("input/14")

map_width = 101
map_height = 103


@dataclasses.dataclass
class Position:
	x: int
	y: int

	def __add__(self, other: "Position") -> "Position":
		return Position(self.x + other.x, self.y + other.y)

	def __hash__(self) -> int:
		return hash((self.x, self.y))


@dataclasses.dataclass
class Robot:
	position: Position
	velocity: Position

	def walk(self) -> None:
		self.position += self.velocity
		while self.position.x >= map_width:
			self.position.x -= map_width
		while self.position.x < 0:
			self.position.x += map_width
		while self.position.y >= map_height:
			self.position.y -= map_height
		while self.position.y < 0:
			self.position.y += map_height


def parse_position(value: str) -> Position:
	values = value.split(",")
	return Position(int(values[0]), int(values[1]))


robots: list[Robot] = []


def draw_robots() -> None:
	positions: set[Position] = set()
	for robot in robots:
		positions.add(robot.position)
	for y in range(map_height):
		for x in range(map_width):
			if Position(x, y) in positions:
				print("#", end="")
			else:
				print(" ", end="")
		print()


def all_unique() -> bool:
	positions: set[Position] = set()
	for robot in robots:
		if robot.position in positions:
			return False
		positions.add(robot.position)
	return True


for line in lines:
	position = line[line.find("p=") + 2:line.find(" ")]
	velocity = line[line.find("v=") + 2:]
	robots.append(Robot(parse_position(position), parse_position(velocity)))

seconds = 0

for _ in range(100):
	seconds += 1
	for robot in robots:
		robot.walk()

quadrants = [0, 0, 0, 0]

for robot in robots:
	if robot.position.x < map_width // 2:
		if robot.position.y < map_height // 2:
			quadrants[0] += 1
		elif robot.position.y > map_height // 2:
			quadrants[1] += 1
	if robot.position.x > map_width // 2:
		if robot.position.y < map_height // 2:
			quadrants[2] += 1
		elif robot.position.y > map_height // 2:
			quadrants[3] += 1

print("Part 1:", quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

while True:
	seconds += 1
	for robot in robots:
		robot.walk()
	if all_unique():
		break

print("Part 2:", seconds)
