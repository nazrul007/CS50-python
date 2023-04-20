# Problem description: https://cs50.harvard.edu/python/2022/psets/0/tip/
#
# dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), 
# remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 
# 50.0.
# percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
# remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 
# 0.15.
# Assume that the user will input values in the expected formats.

def main():
    """
    main driver function provided by assignment. It asks for total meal amount, tip percent and 
    then calculates the actial tip. 
    """    
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d) -> float:
    """
    dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a 
    decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as 
    input, it should return 50.0.

    Args:
        d (str): str representation of dollars. For example, $50.00 
    
    Returns:
        float: dollar in decimal. For example, 50.0 
    """
    # remove the dollar sign 
    dollar_sign, dollar = d.split("$")

    # convert to float 
    return float(dollar)

def percent_to_float(p) -> float:
    """
    percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
    remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should 
    return 0.15.

    Args:
        p (str): percentage. For example, 15%.

    Returns:
        float: percentage in decimal. For example, 0.15
    """    
    digit, percent = p.split("%")
    return float ( float(digit)/100)

if (__name__== "__main__"):
    main()