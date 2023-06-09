# Problem description: https://cs50.harvard.edu/python/2022/psets/3/outdated/
# 
# Hint: https://docs.python.org/3/library/stdtypes.html#string-methods 
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# https://docs.python.org/3/library/string.html#format-string-syntax

import re

# Expected format: September 8, 1636
def reformat_date(d:str) -> str: 
    """
    Reformats a date string to YYYY-MM-DD format. 

    Args:
        d (str): Date format in another format. For example, September 8, 1636

    Returns:
        str: Date string formated in YYYY-MM-DD
    """

    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    new_date = ""
    
    m, d, y = d.split(" ")  
    #print(f'Month: {m} Day: {d} Year: {y}')
    
    try: 
        MM = month_list.index(m.strip()) + 1
        #print(f'Month: {MM:02}') 
    except ValueError as ve: 
        #print(f"Ran into a problem while converting month: [{m}]")
        MM = 0
        raise Exception("Incompatible date format found", ve)
    
    try: 
        DD = d.split(",")[0]
        #print(f'Day: {int(DD.strip()):02}')
    except (Exception): 
        #print(f"Ran into a problem while converting day: [{d}]")
        DD = 0

    #print(f'Year: {y.strip():04}')
    day = int(DD.strip())
    if (day > 31):
        raise Exception("Invalid date format found. Day in a month can not be greater than 31")

    new_date = f'{y.strip():04}-{MM:02}-{day:02}'

    return new_date  

# Expected format: MM/DD/YYYY 
def reformat_date_middle_endian(d:str) -> str: 
    """
    Reformats a date string to YYYY-MM-DD format. 

    Args:
        d (str): A date string in MM/DD/YYYY

    Returns:
        str: Date string formated in YYYY-MM-DD
    """


    new_date = ""
    m, d, y = d.split("/")

    month = int(m.strip())
    if (month > 12):
        raise Exception("Invalid date format found. Month must be between 1 to 12.")
    
    day = int(d.strip())
    if (day > 31): 
        raise Exception("invalid date format found. Day must not be greater than 31.")

    new_date = f'{y.strip():04}-{month:02}-{day:02}'

    return new_date

    
def main(): 
    """
    A program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 
    or September 8, 1636, wherein the month in the latter might matches the supplied format. Then output that same 
    date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. 
    Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 
    days.
    """    
    
    while True: 
        date = input("Date: ").strip()
    
        digit = re.search(r'\d+$', date)
        
        if (date.find(",") != -1) and (digit is not None):  
            try: 
                print( reformat_date(date) )
                break
            except Exception: 
                continue
            
        elif date.find("/"): 
            try: 
                print ( reformat_date_middle_endian(date) )
                break
            except Exception:
                continue
        else:
            continue
        

if __name__== "__main__":
    main()
