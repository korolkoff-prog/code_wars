def is_pangram(st):
	return len(set([c for c in st.lower() if c.isalpha()])) == 26

# This is pangrams
print(is_pangram('The quick brown fox jumps over the lazy dog.'))
print(is_pangram('Cwm fjord bank glyphs vext quiz'))
print(is_pangram('Pack my box with five dozen liquor jugs.'))
print(is_pangram('How quickly daft jumping zebras vex.'))
print(is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))