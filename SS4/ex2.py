def add_fruit(inventory, fruit, quantity=0):
	inventory[fruit] = quantity
	return 
def test(functions):
	if functions == True:
		print("Yay, True")
	else:
		print("LMAO, FALSE!")
	return
# It worked
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test(1)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)
