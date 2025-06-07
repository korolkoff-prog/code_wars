"""
Given the string representations of two integers, return the string representation of the sum of those integers.
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
I have removed the use of BigInteger and BigDecimal in java
Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""


def sum_strings(x, y):
	l, res, carry = max(len(x), len(y)), "", 0
	x, y = x.zfill(l), y.zfill(l)
	for i in range(l-1, -1, -1):
		carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
		res += str(d)
	return ("1" * carry + res[::-1]).lstrip("0") or "0"



print(sum_strings('123', '321'))
print(sum_strings('123', '456'))
print(sum_strings('1111', '11'))
print(sum_strings('1', '99999'))
print(sum_strings('99999', '9'))
print(sum_strings('0888', '0001'))
print(sum_strings('', '111'))
print(sum_strings('0', '0'))
print(sum_strings('', ''))
print(sum_strings('000', '000'))