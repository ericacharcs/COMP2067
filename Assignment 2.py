#Question 1
print("Question #1")
#input
str1 = input('Please enter a string with only alphanumeric characters:')

#valid or not valid + length of string
print('You have entered:',str1)
str1.isalnum()
if str1.isalnum():
    print('This is a valid string')
    print(f"The number of characters in {str1} is:",len(str1))
else:
    print("This is NOT a valid string")


#replacing letter 'e'
if str1.isalnum():
    if str1.find('e') !=-1:
        str2=str1.replace('e','*')
        print(f'The updated string with "e" replaced by "*" is: {str2}')
    else:
        print(f'{str1} does not contain the letter "e"')
else:
    print()



#Question 2
print()
print("Question #2")

#input
str1 = input("Enter the license plate:")

#if statement
if len(str1) ==6 and str1[:3].isalpha() and str1[3:].isdigit():
    print("This plate is a valid older style plate.")
elif len(str1) ==7 and str1[:4].isdigit() and str1[4:].isalpha():
     print("This plate is a valid newer style plate.")
else:
    print("The plate is not valid.")
    
        
    

