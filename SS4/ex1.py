letter_count = {}
string = "ThiS is String with Upper and lower case Letters"

for letter in string.lower():
	if letter != ' ':
		letter_count[letter] = letter_count.get(letter,0) +1
result = list(letter_count.items())
result.sort()
for item in result:
	print ("{0} {1}".format(item[0],item[1]))
