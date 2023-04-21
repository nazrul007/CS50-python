# Problem description: https://cs50.harvard.edu/python/2022/psets/2/twttr/
#
# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts 
# the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

def twitter(): 
    input_str = input("Input: ")
    
    print("Output: ", end="")
    for c in input_str: 
        c_lower = c.lower()
        if (c_lower == "a" or c_lower == "e" or c_lower == "i" or c_lower == "o" or c_lower == "u"):
            pass
        else: 
            print(c, end="")
    print("")

if __name__=="__main__": 
    twitter()