# Problem Definition 
# Implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
# Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the 
# user explicitly, as by passing a str of your own as an argument to input.

def echo(what:str) -> None:
    """outputs that same input in lowercase

    Args:
        what (str): input in lowercase
    """    
    print( what.lower() )

def main(): 
    """main driver function. Prompts the user explicitly, as by passing a str as an argument to input
    """    
    echo( input("What would you like me to repeat? ") )

if __name__=="__main__":
    main()