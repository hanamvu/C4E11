import re

fo = open("alice.txt", "r")
doc = fo.read()
fo.close()
new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', doc)
clean_doc = new_str.strip().split()
letter_count = {}
for word in clean_doc:		
		letter_count[word.lower()] = letter_count.get(word.lower(),0) +1
result = list(letter_count.items())
result.sort()
fo = open("alice_words.txt", "r+")

fo.write("{0}\t\t\t\t{1}\n".format("Word","Count"))
fo.write("++++++++++++++++++++++++++++++\n")
for item in result:
	fo.write ("{0}\t\t\t\t{1}\n".format(item[0],item[1]))
fo.close()
print (letter_count["alice"])
