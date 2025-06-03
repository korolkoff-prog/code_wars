'''
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
'''

def get_count(sentence):
	return sum([ch in 'aeiou' for ch in sentence.lower()])

print(get_count('aEiOuzxcv')) # 5
print(get_count('aaajkjkjAAA')) # 6
print(get_count('zxcvkjKLLj')) # 0
print(get_count('aAuiO')) # 5
print(get_count('aeuAEUll123')) # 6
