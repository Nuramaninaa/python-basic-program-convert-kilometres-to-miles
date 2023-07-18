#python program to convert km(kilometres) to m(miles)

#input from user
km1 = float(input("Enter the speed of motorcycle : "))

#formula : 1 kilometre equals 0.62137 miles
conversion_ratio = 0.62137

m1 = km1 * conversion_ratio

#output of speed
print("Speed of motorcycle is ", m1) 
