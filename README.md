# hm1_313383135
#first home assignment - functions

# task A

def my_func(x1, x2, x3):
    a = x1 + x2 + x3
    b = x2 + x3
    ans = (a * b * x3) / a
    return ans

# task B

def convert(hours, minutes):
    hours_min = hours * 60
    total_min = hours_min + minutes
    time_sec = total_min * 60
    return time_sec
