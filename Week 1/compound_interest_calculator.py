#-------------------------------------------------------------------
# This is a compound interest calculator, along with some challenge
# Written by Leon Wee, March 2018.
# Anyone may freely copy or modify this program.
#-------------------------------------------------------------------

# C = P[(1+r)^n - 1]
# Where:
# C = the compound interest
# P = the principal investment amount (the initial deposit or loan amount)
# r = the annual interest rate (in decimal instead of percentage)
# n = the number of years

def calculateCompountInterest(P, r, n): # create a function that accepts three input which are P, r and n
	C = P*((1+r)**n - 1)
	return C #gives C as output
	
def calculateBalance(C, P): # simple addition function that accept C and P
  B = P + C 
  return B # gives B as output

##this is the challenge data that I gave, your tasks is to calculate the balance of all this data
inputs = [
    {
        "P": 2750,
        "n": 7,
        "r": 0.025
    },
    {
        "P": 1980,
        "n": 6,
        "r": 0.034
    },
    {
        "P": 4637,
        "n": 3,
        "r": 0.04
    },
    {
        "P": 100,
        "n": 100,
        "r": 0.034
    },
    {
        "P": 1257,
        "n": 6,
        "r": 0.048
    },
    {
        "P": 6745,
        "n": 7,
        "r": 0.012
    }
]

for input in inputs:
  print(calculateBalance(calculateCompountInterest(input["P"], input["r"], input["n"]), input["P"]))