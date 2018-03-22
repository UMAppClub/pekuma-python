#----------------------------------------------------------
# This demo program shows the use of for loop statements
# Written by Leon Wee, March 2018.
# Anyone may freely copy or modify this program.
#----------------------------------------------------------

for x in range(10): # print the message for 10 times, by counting from 0,1,2,3,....,8,9
	print("I love programming!")

for x in range(10):
	if x%2 == 0: # check if the remainder of x divided by 2 is 0, if yes, that means it is indeed an even number
		print(str(x) + " is an even number!")
	else: # so logically speaking, if x is not even, then it is odd!
		print(str(x) + " is an odd number!")