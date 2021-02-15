import os
costPerFoot = .87

print(" Cost Calculation Program for Fiber Optics")
compName= input("Please enter the company name: ")
feet = input("Please enter the feet of fiber optics to install: ")
Val = (costPerFoot * int (feet))
print( "Cost calucation for the company", compName, "Fiber Optics per foot at", feet, "feet total is $", Val, ".")
os.system("pause")