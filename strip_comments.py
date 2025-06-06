"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out. 
"""


def strip_comments(string, markers):
	flag_delete = False
	result = ''
	
	for ch in string:
		if ch in markers:
			flag_delete = True
		if flag_delete and ch == '\n':
			flag_delete = False
			result = result.rstrip(' \t')
		if not flag_delete:
			result += ch
	
	return result.rstrip(' \t')


def strip_comments_new(string, markers):
	parts = string.split('\n')
	for s in markers:
		parts = [v.split(s)[0].rstrip() for v in parts]
	return '\n'.join(parts)
