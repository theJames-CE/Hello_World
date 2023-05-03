# Assignment: Hello World!

# 1. TASK: print "Hello World"
print( "Hello World" )

# 2. print "Hello (your name)!" with the name in a variable
name = "James"
print( "Hello", name, "!" )	# with a comma
print( "Hello " + name + "!" )	# with a +

# 3. print "Hello (favorite number)!" with the number in a variable
number = 100
print("Hello" , 100, "!" )	#(favorite  number) with a comma
print( "Hello " + str(100) + "!")	# (favorite number) with a +	-- this one should give us an error!

# 4. print "I love to eat (favorite food 1) and (favorite food 2)." with the foods in variables
fave_food1 = "oysters"
fave_food2 = "chicken and dumplings"
print( "I love to eat {} and {}.".format(fave_food1,fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string