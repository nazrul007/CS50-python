# Problem description: https://cs50.harvard.edu/python/2022/psets/3/grocery/
# Hint: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

def print_dict(d:dict):
    """
    Prints the content of the dictionary. For example, 
       1 MANGO
       2 MILK 
    Does not pluralize the items (based on instructions). 

    Args:
        d (dict): A dictionary of grocery list 
    """        
    keys = sorted(list(d))
    
    for key in keys: 
        print(f'{d.get(key)} {key}') 
    
def grocery_list(): 
    """
    Implements a program that prompts the user for items, one per line, until the user inputs control-d 
    (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all 
    uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted 
    that item. Treats the user’s input case-insensitively.
    """    
    item_dict = {}

    try:
        while (True): 
            # ignore case for item - use uppercase 
            item = input().strip().upper()
            
            try: 
                # check if key is in dict 
                if item in item_dict:
                    item_dict[item] += 1   # increment the count of the item 
                else:
                    # key is not present in dict 
                    item_dict[item] = 1   # first item in the grocery list 
            except (KeyError):
                continue   # ignore key error and contiue to next prompt
    except (EOFError):  # user pressed control-d 
        print_dict(item_dict)  # print out the grocery list 
        exit  
         
if __name__=="__main__":
    grocery_list()
