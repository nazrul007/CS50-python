# Problem description: https://cs50.harvard.edu/python/2022/psets/2/camel/
#
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop. For 
# instance, if s is a str, you could print each of its characters, one at a time, with code like:
# for c in s:
#     print(c, end="")

def main(): 
    camelStr = input("camelCase: ").strip()
    print("snake_case: ", end="")
    for c in camelStr: 
        if c.isupper(): 
            print("_", end="")
            print(c.lower(), end="")
        else: 
            print(c, end="")
    print("\n")
    

if __name__== "__main__": 
    main()