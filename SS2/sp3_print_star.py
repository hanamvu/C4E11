stars = 27
rows = 1
print("Print {0} x {1} stars!".format(stars,rows))
for i in range(rows):
	for j in range(stars):
		print("*",end = '')
print()

stars = 31
rows = 1
print("Print {0} (stars and xs) x {1} !".format(stars,rows))
for i in range(rows):
	for j in range(stars):
		print("x*",end = '')
	print()

stars = 16
rows = 9
print("Print {0} (stars and xs) x {1} !".format(stars,rows))
for i in range(rows):
	for j in range(stars):
		print("x*",end = '')
	print()