clouthes = ["T-Shirt","Sweater"]
print("Hello, welcome to my shop\n")
while (True):
	comment = input("Welcome to our shop, what do you want (C, R, U, D)? ")
	if comment.upper()=="C":
		new_item = input("Enter new item: ")
		clouthes.append(new_item.capitalize())
	elif comment.upper()=="R":
		print(end='')
	elif comment.upper()=="U":
		pos = int(input("Update position? "))
		if pos <= len(clouthes):
			new_item = input("Enter new item: ")
			clouthes[pos-1] = new_item.capitalize()
		else:
			print("Sorry, your item is out of sale!")
	elif comment.upper()=="D":
		pos = int(input("Delete position? "))
		if pos <= len(clouthes):
			clouthes.pop(pos-1)
		else:
			print("Sorry, your item is out of sale!")
	else:
		print("Allahu akbar! We're in reconstructing and can't serve you. See you again!")
	# items =[", "+clouthe for clouthe in clouthes if clouthes.index(clouthe)>0]
	# items.insert(0,clouthes[0]) 
	# print("Our items: {0}".format(items))
	# print("\n")
	print("Our items: ",end='')
	for item in clouthes:
		if clouthes.index(item)<len(clouthes)-1:
			print(item,end=', ')
		else:
			print(item+"\n")
		
