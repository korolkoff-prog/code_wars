"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
	result = ''

	for ch in message:
		if ch.islower():
			alphabet = 'abcdefghijklmnopqrstuvwxyz'
		else:
			alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

		if ch in alphabet:
			index = alphabet.index(ch)
			new_index = (index + 13) % 26
			result += alphabet[new_index]
		else:
			result += ch

	return result


print(rot13('test')) # grfg
print(rot13('aA bB zZ 1234 *!?%')) # nN oO mM 1234 *!?%