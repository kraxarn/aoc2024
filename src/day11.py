def get_stone_count(stop: int) -> int:
	line: str = read_lines("input/11")[0]
	stones = [int(stone) for stone in line.split()]

	for blink_count in range(stop):
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

	return len(stones)


print("Part 1:", get_stone_count(25))
print("Part 2:", get_stone_count(75))
