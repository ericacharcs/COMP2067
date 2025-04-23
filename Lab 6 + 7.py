#input statement
str =input("Enter credit card number:")

#variables
ccNum = int(str)
length = len(str)
ffNum = ccNum // 10**(length - 4)
print(ffNum)

#Luhn algorithm 
counter = 0
sum = 0 

while(ccNum > 0):
    
    lastDigit = ccNum % 10
    if counter % 2 == 1:
        lastDigit *= 2
        if lastDigit > 9:
            sum+= lastDigit % 10
            sum+= lastDigit // 10
        else:
            sum += lastDigit
        
    else:
        sum += lastDigit
    
    ccNum //= 10
    counter += 1

if sum % 10 == 0:
    
#determining issuer
    if ffNum == 1800 or ffNum == 2131:
        print(f"The Credit Card {str} is valid and the issuer is JCB")

    elif ffNum == 2014 or ffNum == 2149:
        print(f"The Credit Card {str} is valid and the issuer is Diner's Club")

    elif ffNum == 6011:
        print(f"The Credit Card {str} is valid and the issuer is Discover")
        
    else:
        ffNum //= 10
        if ffNum == 300 or ffNum == 301 or ffNum == 302 or ffNum == 303 or ffNum == 304 or ffNum == 305:
            print(f"The Credit Card {str} is valid and the issuer is Diner's Club")
        else:
            ffNum //= 10
            if ffNum == 34 or ffNum == 37:
                print(f"The Credit Card {str} is valid and the issuer is American Express")
            elif ffNum == 36 or ffNum == 38:
                print(f"The Credit Card {str} is valid and the issuer is Diner's Club")
            elif ffNum == 51 or ffNum == 52 or ffNum == 53 or ffNum == 54 or ffNum == 55:
                print(f"The Credit Card {str} is valid and the issuer is MasterCard")
            else:
                ffNum //= 10
                if ffNum == 3:
                    print(f"The Credit Card {str} is valid and the issuer is JCB")
                elif ffNum == 4:
                    print(f"The Credit Card {str} is valid and the issuer is Visa")
                else:
                    print("The Credit Card is invalid")
                    
else:
    print("Not valid")


