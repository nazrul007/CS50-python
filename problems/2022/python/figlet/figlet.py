# Problem description: https://cs50.harvard.edu/python/2022/psets/4/figlet/
# 
# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.

from pyfiglet import Figlet 
import random
import sys

def main(): 
    """
    Prompts the user for a str of text. Outputs that text in the desired font or a random font.
    """    
    

    if len(sys.argv) == 1: 
        figlet = Figlet()
        font_list = figlet.getFonts()
        f = random.choice(font_list)   # pick a font at random 
        figlet.setFont(font=f)
        s = input("Input: ").strip()
        print("Output: ")
        print(figlet.renderText(s))    # prints out the input text 
    elif  len(sys.argv) == 3: 
        if (sys.argv[1]) == "-f" or (sys.argv[1]) == "--font": 
            try: 
                figlet = Figlet()
                figlet.setFont(font=sys.argv[2])  # uses the font 
                s = input("Input: ").strip()
                print("Output: ")
                print(figlet.renderText(s))
            except Exception:
                print("Invalid usage")    # invalid font 
                sys.exit(1)
        else:
            print("Invalid usage")
            sys.exit(1)
    else: 
        print("Invalid usage")   # invalid # of options 
        sys.exit(1)

if __name__=="__main__": 
    main()

        





