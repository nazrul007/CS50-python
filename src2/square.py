def main():
    print_square(8)
    print_square_1(10)

def print_square(size:int): 
    """
    Prints out a square with '#'.

    Args:
        size (int): Size of the square
    """
    for i in range(size):
        for j in range(size):
            print("#", end="")
        
        print()

def print_square_1(size:int):
    """
    Prints out a square using '$'

    Args:
        size (int): Size of the square
    """    
    for i in range(size):
        print_row(size)

def print_row(width:int): 
    """
    Print out a row

    Args:
        width (int): Width of the row
    """    
    print("$" * width)

if (__name__ == "__main__"):
    main()