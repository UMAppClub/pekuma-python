#---------------------------------------------------
# This demo program shows the use of IF statements
# Written by Leon Wee, March 2018.
# Anyone may freely copy or modify this program.
#---------------------------------------------------

weight = eval(input("Please enter your weight:\n")) # accept some input from user

if weight >= 100: # check if the weight is larger than 80
	print("Time to get some exercise bruh! >_<")
elif weight >= 50:
	print("Great, keep it up! ^_^")
else: # if the weight is less than 50, this part get executed!
	print("You probably need to eat more! ._.")