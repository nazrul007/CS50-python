# Problem Definition
# Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down,
# a la YouTube’s 0.75 playback speed, or even by having them pause between words.
#
# In a file called playback.py, implement a program in Python that prompts the user for input and then
# outputs that same input, replacing each space with ... (i.e., three periods).
#
# Hints
# Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.

def replace(what: str) -> str:
    """outputs that same input, replacing each space with ...

    Args:
        what (str): input string 

    Returns:
        str: input string replaced each space with ...
    """

    return what.replace(' ', '...')

def main():
    """main driver function that prompts the user for input and shows the playback string 
    """
    userInput = str(input("What would you like me to repeat? "))
    print(replace(userInput))


if (__name__ == "__main__"):
    main()
