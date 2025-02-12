#  Implement a Python function called check_password_strength that takes a password string as input.

# ●       The function should check the password against the following criteria:

# ○       Minimum length: The password should be at least 8 characters long.

# ○       Contains both uppercase and lowercase letters.

# ○       Contains at least one digit (0-9).

# ○       Contains at least one special character (e.g., !, @, #, $, %).

# ●       The function should return a boolean value indicating whether the password meets the criteria.

# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

# ●       Provide appropriate feedback to the user based on the strength of the password.
# 
# --------------------------------------------------------------------------------------------------------------------- 
import re

def check_password_strength(password):
    sc=['!','@','#','$','%','&','*','/','_','-']

    #check password length 
    if(len(password)<8):
        return False    
    #check for digits in password
    valIsdigit= any(char.isdigit() for char in password)
    #check for UpperCases in password
    valisUpper= any(char.isupper() for char in password)
    #check for LowerCases in password 
    valisLower = any(char.islower() for char in password)
    #check for Special characters in Password
    valSpecialChar= any(char in sc for char in password)

#check if all casses are passed or not 
    if(valSpecialChar and valisLower and valisUpper and valIsdigit):
        return True
    else:
        return False
    

passwrd=input("enter your password here: ")
strnthVal=check_password_strength(passwrd)
if(strnthVal):
    print("password is strong")
else:
    print("password is not strong")


    
