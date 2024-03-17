# taking values of variables
p = int(input("Enter the value of p: "))

r = int(input("Enter the value of r: "))

n = int(input("Enter the value of n: "))

t = int(input("Enter the value of t: "))

# simple interest

S_I = (p * r * t ) /100
print("the simple interest is",S_I) 


# compound interest
x = int((1 + (r/n)) ** (n * t))

C_I= p * x 
print("the compound interest is",C_I) 


# Annuity plan
pmt = int(input("Enter the periodic payment : "))

A = (pmt * (x - 1)) / (r/n)
print("The annuity plan is",A)