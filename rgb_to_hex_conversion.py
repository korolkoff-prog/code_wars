"""
The rgb function is incomplete. 
Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
"""


def rgb(r, g, b):
	if r > 255:
		r = 255
	elif r < 0:
		r = 0

	if g > 255:
		g = 255
	elif g < 0:
		g = 0

	if b > 255:
		b = 255
	elif b < 0:
		b = 0

	r = hex(r)[2:]
	g = hex(g)[2:]
	b = hex(b)[2:]

	if len(r) == 1:
		r = '0' + r
	if len(g) == 1:
		g = '0' + g
	if len(b) == 1:
		b = '0' + b

	return f'{r.upper()}{g.upper()}{b.upper()}'


print(rgb(0, 0, 0))
print(rgb(255, 255, 255))
print(rgb(148, 0, 211))
print(rgb(255, 255, 300))