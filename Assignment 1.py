#Question 1

#Constants
COSTCOMP = ((6*60)/45)*15.92
COSTTP = 2.09
COSTSP = 0.87
PI = 3.14

#Inputs
print("Question 1")
print()
sideLength=float(input("Enter the side length of the finished square garden (between 10-20 feet):"))
spacing=float(input("Enter the spacing between the plants (in feet):"))
print()

#Variables
radius = round(sideLength/4,2)
circumference = round(2*PI*radius,2)
circumferenceSemi = round(circumference*2,2)
numPC = round(circumference/spacing)
numPSC = round(circumferenceSemi/spacing)
numTotal = round(numPC + numPSC)
CostTP = round(COSTTP*numPC,2)
CostSP = round(COSTSP*numPSC,2)
CostTotal = round(CostTP + CostSP,2)
CostEverything = round(CostTotal + COSTCOMP,2)

#Displays
print(f"Number of plants for circle (tall plants): {numPC}")
print(f"Number of plants for semicircle (small plants): {numPSC}")
print(f"Total number of plants for garden: {numTotal}")
print(f"Cost of tall plants: ${CostTP}")
print(f"Cost of small plants: ${CostSP}")
print(f"Total cost of plants for the flower bed: ${CostTotal}")
print(f"Total cost paid to company to complete the flower bed: ${COSTCOMP}")
print(f"Total cost of constructing the flower bed: ${CostEverything}")
print()
print()

#Question 2
print("Question 2")
print()
#variables
str = 'AGCTTACCGGATCAGGCTAGCTAGCTAGCTTAGCTGAGCTG'
Acount = str.count('A')
Tcount = str.count('T')
Ccount = str.count('C')
Gcount = str.count('G')
GCcontent = round(((Gcount + Ccount)/len(str))* 100,2)


#displays 
print(f"DNA Sequence: {str}")
print(f"A Count: {Acount}")
print(f"T Count: {Tcount}")
print(f"C Count: {Ccount}")
print(f"G Count: {Gcount}")
print(f"GC Content: {GCcontent}%")
