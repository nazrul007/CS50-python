import sys

def main():
    x = get_int()
    print(f"X is {x}")
    print("hello, my name is", sys.argv[1])

def get_int()->int:
    """
    Prompts user for an integer input called 'X'

    Returns:
        int: Integer input
    """
    while True:
        try:
            x = int(input("What's X? " ))
        except ValueError:
            print("X is not an integer")
        else:
            break
    return x

if (__name__=="__main__"):
    main()