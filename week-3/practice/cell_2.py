#input from user
m = float(input("Enter mass in kilograms: "))

# cconstant value for the spead of light in m/s 
c= 299792458

# calculating energy using einstein's equation
energy = m * c ** 2

# displaying the result 
print(f"the energy equivalent to {m}kg of mass is {energy} joules.")