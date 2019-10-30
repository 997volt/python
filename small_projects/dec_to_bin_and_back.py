# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:18:17 2019

@author: Piotr Hałaburdzin
"""

def show_summary():
    print("Welcome in simple decimal to binary and binary to decimal converter!")
    print("Just write your decimal or binary number and it will do the rest.")
    print("To exit the program you can write \"e\" instead of number")


def get_user_input():
    user_input = input ("Write number to convert (or 'e' to exit): ")
    

    #exit program with 'e' passed from user
    if(user_input == "e"):
        print("User request - exiting program")
        return "e"
    
    #getting input as long as number is passed
    number = 0
    while(number == 0):
        try:
           number = int(user_input)
           print("Input number value is:", number)
        except ValueError:
           print(user_input, "is not a numeric input. Let's try again")
           user_input = input ("Write number to convert: ")
           
    return number

# converts a decimal (integer) input to binary (string)
def convert_to_bin(decimal):
    print("Your decimal number to convert is: ", decimal)
    binary = ""

    while(decimal > 0):        
        if(decimal % 2 == 0):
            binary = "0" + binary
            decimal = decimal/2            
        else:
            binary = "1" + binary  
            decimal = (decimal - 1)/2

    print("Your number converted to binary is:", binary)
    return binary


def main():
    show_summary()
    
    while(True):
        user_input = get_user_input()
        
        #exit program with 'e' passed from user 
        if(user_input == "e"):
            return 1
        
        convert_to_bin(user_input)
    
    return 0
    

main()