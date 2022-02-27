
# task A
def my_func(x1, x2, x3):
    a = x1 + x2 + x3
    b = x2 + x3
    ans = (a * b * x3) / a
    return ans

# print(my_func(2,5,7))
# task B


def convert(hours, minutes):
    hours_min = hours * 60
    total_min = hours_min + minutes
    time_sec = total_min * 60
    return time_sec


# print(convert(1,3))
