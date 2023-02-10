# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:07:37 2023
@author: Sukoluhle Ndlovu
This function takes a 10 digit or 13 didgit ISBN and returns "Valid" if the ISBN is valid and "Invalid" if the 
ISBN is not valid.It uses the ISBN formula to calculate the checksum and determine whether the ISBN is valid or not.
If the ISBN is a 10 digit ISBN, it will add the "978" prefix before calculating the checksum.
"""

def isbn13(isbn):
    # check if isbn is 10 or 13 digits
    if len(isbn) == 10:
        # calculate sum of products
        sum = 0
        for i in range(len(isbn)):
            if isbn[i] == 'X':
                sum += 10
            else:
                sum += int(isbn[i]) * (10-i)
        # check if divisible by 11
        if sum % 11 == 0:
            # convert to ISBN-13
            isbn13 = '978' + isbn[:-1] + str(11 - (sum % 11))
            return isbn13
        else:
            return 'Invalid'
    elif len(isbn) == 13:
        # calculate sum of products
        sum = 0
        for i in range(len(isbn)):
            sum += int(isbn[i]) * (1 if i % 2 == 0 else 3)
        # check if divisible by 10
        if sum % 10 == 0:
            return 'Valid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'
   #Run the following statements to check if the ISBN number is Valid or Invalid 
print(isbn13("9780316066525"))
print(isbn13("0330301824"))
print(isbn13("0316066524")) 

