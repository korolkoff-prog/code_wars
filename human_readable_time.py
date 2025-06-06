"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures.
"""

def make_readable(seconds):
	return f'{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}'


print(make_readable(0))
print(make_readable(59))
print(make_readable(3600))
print(make_readable(86399))