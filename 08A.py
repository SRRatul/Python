# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:09:12 2024

@author: Salvir Rahman Ratul
"""

def reverse_string(s):
    return s[::-1]
def main():
    user_string = input("Enter the string->  ")
    reversed_string = reverse_string(user_string)
    print(f"The user string : {user_string}")
    print(f"The reverse string: {reversed_string}")
if __name__ == "__main__":
    main()