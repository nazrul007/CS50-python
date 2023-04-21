# Problem description: https://cs50.harvard.edu/python/2022/psets/2/plates/
# 
# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, 
# with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
#
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an 
# acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str) -> bool:
    valid = False
    size = len(s)

    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if (size >= 2 and size <= 6):

        #print(f"Size: {size}")

        # No periods, spaces, or punctuation marks are allowed
        if s.isalpha():
            valid = True
            #print ("Aphabets")
        elif (not s.isalpha()) and s.isalnum(): 

            #print("Alphanumeric")

            # All vanity plates must start with at least two letters
            two_chr = s[0:1]
            if two_chr.isalpha():
                #print("Starts with two character")

                # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 
                # would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used 
                # cannot be a ‘0’.”
                if ends_with_num(s): 
                    valid = True
                    #print("Ends with num")

    return valid

def ends_with_num(s:str) -> bool:
    """Returns tur if the input string ends with all numbers. 

    Args:
        s (str): input string 

    Returns:
        bool: true if the string ends with all numbers and does not start with zero
    """    
    i = 0
    valid = False

    for c in s:
        if c.isalpha(): 
            i += 1
        else: # first non alphabet character  
            
            # check if the substring is all digits  
            end = s[i:] 
            #print(f"Digits {end}")
            if (not end.startswith("0")):
               if end.isdigit():
                    valid = True
                    #print("Ends with digits")
    return valid 

        
if __name__=="__main__":
    main()