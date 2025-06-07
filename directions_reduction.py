def dir_reduc(arr):
	stack = []

	for current_dir in arr:
		if len(stack) == 0:
			stack.append(current_dir)
		elif current_dir == "NORTH" and stack[-1] == "SOUTH" or current_dir == "SOUTH" and stack[-1] == "NORTH":
			stack.pop()
		elif current_dir == "WEST" and stack[-1] == "EAST" or current_dir == "EAST" and stack[-1] == "WEST":
			stack.pop()
		else:
			stack.append(current_dir)		

	return stack


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) # WEST
print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"])) # NORTH, WEST, SOUTH, EAST