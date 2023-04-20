"""
Problem description: https://cs50.harvard.edu/python/2022/psets/0/einstein/

Even if you haven’t studied physics (recently or ever!), you might have heard that E=MC^2 wherein 
  E represents energy (measured in Joules), 
  m represents mass (measured in kilograms), and 
  c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. 
Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer 
(in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will 
input an integer.

Hints
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that int can convert a str to an int, per docs.python.org/3/library/functions.html#int.
Recall that Python comes with several built-in functions, per docs.python.org/3/library/functions.html.
"""


def e_mc2(m:int) -> int: 
    """Prompts user for m and calculates mc^2.
    
    Args:
        m (int): represents mass (measured in kilograms)

    Returns:
        int: E, represents energy (measured in Joules)
    """
    # c represents the speed of light (measured approximately as 300000000 meters per second)
    c = 300000000
    
    # alternative to usig pow function 
    #return m * c**2

    # calculate and return mc^2 
    return m * pow(c, 2)

def main(): 
    # ask user for m, represents mass (measured in kilograms)
    userInput = int(input("m: "))

    # show calculated mc^2 digits with ,
    print ( f'{e_mc2(userInput):,}' )
    
    # show calculated mc^2 digits
    #print (e_mc2(userInput))

if (__name__=="__main__"):
    main()