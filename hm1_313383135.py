
# task A
def my_func(x1=None, x2=None, x3=None):
    try:
        x1 = float(x1)
        x2 = float(x2)
        x3 = float(x3)
        denominator = x1 + x2 + x3
        if denominator != 0:
            a = x2 + x3
            ans = (denominator * a * x3) / denominator
            return f"The value is: {ans}"
        else:
            return "Not a number – denominator equals zero"
    except:
        return "Error: parameters should be double"


# print(my_func(1, 2, 3))


# task B
def convert(hours=0, minutes=0):
    try:
        hours = float(hours)
        minutes = float(minutes)
        if hours >= 0 and minutes >= 0:
            hours_min = hours * 60
            total_min = hours_min + minutes
            seconds = total_min * 60
        return f"It will be {int(seconds)} seconds"
    except:
        return "Input error!"


# print(convert(1.75, 13))

