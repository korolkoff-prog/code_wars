"""
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present. 
"""

from itertools import permutations as get_permutations


# Time limit error
def permutations_first_version(s):
    def permute(a, n):
        if n == 1:
        	if ''.join(a) not in result:
	            result.append(''.join(a))
	            return
        
        for i in range(n):
            permute(a, n-1)
            if n % 2 == 0:
                a[i], a[n-1] = a[n-1], a[i]
            else:
                a[0], a[n-1] = a[n-1], a[0]
    
    result = []
    permute(list(s), len(s))
    return result

# Интересное решение)
def permutations_v(s):
	if len(s) == 0:
    	return []
    elif len(s) == 1:
    	return [s]
    else:
    	return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))


def permutations(s):
	perms = set(get_permutations(s))
	result = []
	
	for item in perms:
		result.append(''.join(item))

	return result


print(permutations('abc'))
print(permutations('aabb'))