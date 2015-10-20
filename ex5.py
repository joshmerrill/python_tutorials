# define variables
my_name = 'Josh A Merrill'
my_age = 34		# not a lie
my_height = 76	# inches
my_weight = 200	# lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Blonde'

# define variables inside strings
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's fairly heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)