# Problem description: https://cs50.harvard.edu/python/2022/psets/2/nutrition/
# The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information 
# for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the 
# posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the 
# stores.”
#
# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit 
# (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster 
# for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly 
# as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

def main(): 
    fruits_dict  = [
        {"Name": "Apple", "Calories": "130"},
        {"Name": "Avocado", "Calories": "50"},
        {"Name": "Banana", "Calories": "110"},
        {"Name": "Cantaloupe", "Calories": "50"},
        {"Name": "Grapefruit", "Calories": "60"},
        {"Name": "Grapes", "Calories": "90"},
        {"Name": "Honeydew Melon", "Calories": "50"},
        {"Name": "Kiwifruit", "Calories": "90"},
        {"Name": "Lemon", "Calories": "15"},
        {"Name": "Lime", "Calories": "20"},
        {"Name": "Nectarine", "Calories": "60"},
        {"Name": "Orange", "Calories": "80"},
        {"Name": "Peach", "Calories": "60"},
        {"Name": "Pear", "Calories": "100"},
        {"Name": "Pineapple", "Calories": "50"},
        {"Name": "Plums", "Calories": "70"},
        {"Name": "Strawberries", "Calories": "50"},
        {"Name": "Sweet Cherries", "Calories": "100"},
        {"Name": "Tangerine", "Calories": "50"},
        {"Name": "Watermelon", "Calories": "80"},
    ]
    
    f = input("Item: ").strip()
    
    #print(f)

    for fruit in fruits_dict: 
        
        #print(fruit["Name"])
        
        if (f.lower() == fruit["Name"].lower()):
            print(f'Calories: {fruit["Calories"]}')
            break
        else: 
            continue 
    
if __name__=="__main__": 
    main()
