"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
They would like your help with an application form that will tell prospective members 
which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

"""

def open_or_senior(data):
	return ["Senior" if age >= 55 and k > 7 and k <= 26 else "Open" for age, k in data]


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))
print(open_or_senior([(37, 17), (67, -1), (27, 5), (89, 7)]))