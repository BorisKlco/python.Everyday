"""
Bin search

define low, first element of array, 0
define high, len of array
create loop while low < high
define mid point of array as m
m = math floor for float nums, low + (high-low)/2
value is array[m]
if value == searching n --> return True,indexOf,value
if value > n --> we are over so we limit our high point --> high = m
else value < n --> we need set our low point to out value + 1 , element next to our value.
return -1 if searching n is not in array
"""
import math

primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]


def binSearch(array, num):
    lo = 0
    hi = len(array)

    while lo < hi:
        m = math.floor(lo + (hi - lo) / 2)
        v = primes[m]
        # print(lo, hi)
        if v == num:
            return m
        if v > num:
            hi = m
        else:
            lo = m + 1
    return -1


print(f"Index of 73 is {binSearch(primes,73)}")
