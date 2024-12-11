line: str = read_lines("input/11")[0]

stones = [int(stone) for stone in line.split()]

for blink_count in range(25):
	i = 0
	while True:
		stone = stones[i]
		if stone == 0:
			stones[i] = 1
			i += 1
		elif len(str(stone)) % 2 == 0:
			digits = str(stone)
			stones[i] = int(digits[:len(digits) // 2])
			stones.insert(i + 1, int(digits[len(digits) // 2:]))
			i += 2
		else:
			stones[i] = stone * 2024
			i += 1
		if i >= len(stones):
			break

print("Part 1:", len(stones))
