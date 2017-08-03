import re
import string
fo = open("alice.txt", "r")
doc = fo.read()
fo.close()
# Su dung regex xoa het punctuation, tuy nhien exeption o ky hieu quote, UNIX ko bi. 
# wtf
new_str = re.sub('['+string.punctuation+'‘’“”]', ' ', doc)
# Xoa space va \t \r
clean_doc = new_str.strip().split()

letter_count = {}
col_width = 0
for word in clean_doc:		
	letter_count[word.lower()] = letter_count.get(word.lower(),0) +1
	if col_width < len(word.lower()):
		col_width = len(word.lower())
result = list(letter_count.items())
result.sort()
fo = open("alice_words.txt", "r+")
fo.truncate()

fo.write("{0}{1}\n".format("Word".ljust(col_width),"Count"))
fo.write("--------------------\n")
for item in result:
	fo.write ("{0}{1}\n".format(item[0].ljust(col_width),item[1]))
fo.close()
print (letter_count["alice"])
