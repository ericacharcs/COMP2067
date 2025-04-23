#Question 1
print("Question 1:")
#strings and inputs
custAreaCode= str(input("What is the area code you are calling from?"))

custPhoneNum= str(input("What is the phone number you are calling from?"))

calledAreaCode= str(input("What is the area code you are calling?"))

calledPhoneNum= str(input("What is the phone number you are calling?"))

minutes= int(input("In minutes, how long is the call?"))

#Variables
TIMELIMIT = 20
LOWRATE = 10/100
HIGHRATE = 13/100

#print statements and rates 
if custAreaCode != calledAreaCode and minutes>TIMELIMIT:
    price = minutes*LOWRATE
    print(f"The cost of calling from {custAreaCode} - {custPhoneNum} to {calledAreaCode} - {calledPhoneNum} for {minutes} minutes is ${price}")
else:
    price = minutes*HIGHRATE
    print(f"The cost of calling from {custAreaCode} - {custPhoneNum} to {calledAreaCode} - {calledPhoneNum} for {minutes} minutes is ${price}")


#Question 2
print("")
print("Question 2:")

def generate_pascals_triangle(num_rows):
    triangle = []

    for i in range(num_rows+1):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j] for j in range(i + 1)]
        triangle.append(row)

    return triangle

def display_pascals_triangle(triangle):
    for row in triangle:
        print(row)

# Input statements
num_rows = int(input("Enter number of rows: "))

# Generating Pascal's triangle
pascals_triangle = generate_pascals_triangle(num_rows)

# Display
print("\nThe Pascal triangle is as follows:\n")
display_pascals_triangle(pascals_triangle)


#Question 3
print('')
print("Question 3:")


lists = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#magic function 
def magic(lists):
    return [sublist for sublist in lists if sum(sublist)%2 ==0]

result= magic(lists)
print(result)
 
