# Problem description: https://cs50.harvard.edu/python/2022/psets/4/emojize/
# Implement a program that prompts the user for a str in English and then outputs the “emojized” version of that 
# str, converting any codes (or aliases) therein to their corresponding emoji.
#
# Hint: Note that the emoji module comes with two functions, per pypi.org/project/emoji, one of which is emojize, 
# which takes an optional, named parameter called language. You can install it with: pip install emoji

import emoji 

def main(): 
    em = input("Input: ").strip()
    print(emoji.emojize(em))

if __name__== "__main__": 
    main()