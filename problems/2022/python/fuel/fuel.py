# Problem description: https://cs50.harvard.edu/python/2022/psets/3/fuel/
#
# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein 
# each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel 
# is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
#
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not 
# necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
# 
# Hints: 
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, 
# including split.
# Note that you can handle two exceptions separately with code like:
# try:
#    ...
# except ValueError:
#    ...
# except ZeroDivisionError:
#    ...

import math

def main():
    while True:
        try: 
            x, y = input("Fraction: ").split("/")
            
            x_int = int(x)
            y_int = int(y)
            percent = (x_int / y_int) * 100

            if (percent <= 1):
                print("E")
                break
            elif (percent >= 99 and percent <= 100):
                print("F")
                break
            elif (percent <= 100):
                print(f'{round(percent)}%', end="")
                break
            else:
                pass 
        except (ValueError, ZeroDivisionError): 
            pass

if __name__== "__main__":
    main()
