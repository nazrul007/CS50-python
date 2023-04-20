def main():
    x = get_int("What's x? ")
    print(f"X is {x}")

def get_int(prompt:str)->int:
    """
    Prompts user for input. It will keep prompting user until user inputs an integer. 

    Args:
        prompt (str): Prompt string 

    Returns:
        int: Input integer
    """    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()