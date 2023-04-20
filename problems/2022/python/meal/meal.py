# Problem description: https://cs50.harvard.edu/python/2022/psets/1/meal/
# implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or 
# dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be 
# formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, 
# whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
#
# Structure your program per the below, wherein convert is a function (that can be called by main) that converts 
# time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like 
# "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
#
# Hint: 
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, 
# including split, which separates a str into a sequence of values, all of which can be assigned to variables at 
# once. For instance, if time is a str like "7:30", then
# hours, minutes = time.split(":")
# will assign "7" to hours and "30" to minutes.
# Keep in mind that there are 60 minutes in 1 hour.

def main():
    time = input("What time is it? ").strip().lower()
    #print(len(sys.argv))
    time_f = convert(time)

    if (time_f >= 7.0 and time_f <= 8.0): 
        print("breakfast time")
    elif (time_f >= 12.0 and time_f <= 13.0):
        print("lunch time")
    elif (time_f >= 18.0 and time_f <= 19.0): 
        print("dinner time")
    else:
        pass
 
def convert(time:str) -> float: 
    """Converts time in string format to a float in 24 hour format. Supported formats: 
    #:## a.m. and ##:## a.m. 
    #:## p.m. and ##:## p.m.
    For example, 7:30, 7:30 a.m., 18:32, 6:32 p.m., 06:32 p.m.

    Args:
        time (str): time in format #:## or ##:##. It may contain a.m. or p.m. 

    Returns:
        float: time as float in 24 hour clock 
    """    
    am = False
    pm = False

    if time.endswith("a.m."): 
        time_hm = time.removesuffix("a.m.")
    elif (time.endswith("p.m.")): 
        time_hm = time.removesuffix("p.m.")
        pm = True
    else: 
        time_hm = time     

    hours, minutes = time_hm.split(":")

    hrs = float(hours.strip())
    
    if (pm == True):
        hrs += 12.0
    mins = float(minutes.strip())

    cur_time = hrs + mins/60

    return cur_time

if __name__ == "__main__":
    main()
