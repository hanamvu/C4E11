dude_name = input("Hey bro, what's your name?\n")
print("Wanna some joke? Let's begin!")
height = int(input("How height you are? Give me your answear in centimeters please!\n"))
weight = float(input("Excuse me, but how about your weight? This is a private question.\n"))
BMI = weight/((height/100)**2)
if BMI < 16:
	print("Hollyshit {}, YOU ARE SERVERELY UNDERWEIGHT!".format(dude_name))
elif BMI < 18.5:
	print("{0}, you're underweight bro, buy Appeton Weight Gain Milk now!".format(dude_name))
elif BMI < 25:
	print("Hey {}.Normal. How?".format(dude_name))
elif BMI < 30:
	print("Hmm, Overload, Overweight, {} !".format(dude_name))
else:
	print("What can i say, you're like BigMom {}. Obese!".format(dude_name))
