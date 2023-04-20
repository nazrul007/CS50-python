# Problem description: https://cs50.harvard.edu/python/2022/psets/2/coke/
#
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these 
# denominations: 25 cents, 10 cents, and 5 cents.
# 
# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each 
# time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many 
# cents in change the user is owed. Assume that the user will only input integers, and ignore any integer 
# that isn’t an accepted denomination.

def main(): 
    due = 50
    
    print("Amount Due: 50")
    
    try:
        while (due > 0):
            coin_str = input("Insert Coin: ")
            if (coin_str == "25" or coin_str == "10" or coin_str == "5"): 
                coin = int(coin_str)
                due -= coin 
            if (due > 0): 
                print(f"Amount Due: {due}")
            else:
                print(f"Change Owed: {abs(due)}")

    except: 
        pass 
    

if __name__ == "__main__":
    main()