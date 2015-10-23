# define variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x		# print the statement using the raw variable
print "I also said: '%s'." % y	# print the statement using the string variable

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"		# define the variable with a built in string to be defined later

print joke_evaluation % hilarious 		# printing the statement and defining the string to include

w = "this is the left side of..."
e = "a string with a right side."

print w + e		# combining the strings in a print statement