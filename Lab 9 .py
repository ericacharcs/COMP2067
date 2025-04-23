#empty list
lst = []

#calculating factorial 
def NNIfactorial(n):
    s = 1
    for i in range( 1, n + 1):
        s *=i
    lst.append(s)
    return s

#printing the factorial list 
def flst(list):
    print(f"factorial_list = {lst}")

#input statement
n = int(input("Please enter a positive integer between 1 and 20:"))

#list loop 
for j in range(1, n + 1):
    results= NNIfactorial(j)
    print(f"j={j};\t\t {j} != {results}")

flst(lst)
