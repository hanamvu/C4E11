prices = {
	"banana" : 4,
	"apple"	: 2,
	"orange" : 1.5,
	"pear" : 3
}

purchased_items = [('banana', 5),("orange",3)]
total = 0
for item in purchased_items:
	quantity = int(item[1])
	unit_price= int(prices.get(item[0],0))
	wasted_money = quantity*unit_price
	print("{0}, quantity: {1}, unit price: {2}".format(item[0],quantity,unit_price))
	total += wasted_money
	print("Wasted: {0} $".format(wasted_money))
print("Total money wasted: {0} $".format(total))
	
