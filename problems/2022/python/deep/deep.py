# Problem description: https://cs50.harvard.edu/python/2022/psets/1/deep/
# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and 
# Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise 
# output No.

def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
    #print(ans.lower())
    if "42" == ans: 
        print("Yes")
    elif ("forty two" == ans.lower()) or ("forty-two" == ans.lower()):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__": 
    main()