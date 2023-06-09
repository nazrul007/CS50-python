# Problem description: https://cs50.harvard.edu/python/2022/psets/3/taqueria/ 
# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for 
# items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) 
# and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an 
# item. Assume that every item on the menu will be titlecased.
#
# Hint:  docs.python.org/3/library/stdtypes.html#mapping-types-dict

def food_checkout(): 
    food_dict = {
        "baja taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }
    
    total_price = 0.0

    try:
        while (True): 
            # ignore case for item  
            item = input("Item: ").strip().lower()
            
            try: 
                # check if key is in dict 
                if item in food_dict:
                    total_price += food_dict[item]
                    print(f"Total: ${total_price:.2f}") 
                else:
                    # key is not present in dict 
                    continue
            except (KeyError):
                continue   # ignore key error and contiue to next prompt
    except (EOFError):
        exit  # user pressed control-d 
         
if __name__=="__main__":
    food_checkout()
