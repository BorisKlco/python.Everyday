"""
Bubble sort

take bubble[n] 
compere it with bubble[n+1]
if bigger, than swap
otherwise n +=1
"""
bubble = [2, 1, 7, 5, 6, 9, 8, 3, 4]
print("Bubble sort, usorted", bubble)

for i in range(len(bubble) - 1):
    for n in range(len(bubble) - 1 - i):
        if bubble[n] > bubble[n + 1]:
            value_holder = bubble[n]
            bubble[n] = bubble[n + 1]
            bubble[n + 1] = value_holder


print("Bubble sort, sorted", bubble)

print()
# Challenge: Find minimum in subarray
# https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/pc/challenge-find-minimum-in-subarray
finding_minimum_array = [18, 6, 66, 44, 9, 22, 14]


def finding_minimum(array, position):
    """
    set min value and index,
    iterate over array from provided position
    if current value is lower than min value than swap min value for new one
    """

    min_value = array[position]
    min_index = position
    for num in range(min_index, len(array)):
        if array[num] < min_value:
            min_value = array[num]
            min_index = num
    return min_value, min_index


print("Find min value in array from index of x", finding_minimum_array)
print("Min value+Indexof from index of 2:", finding_minimum(finding_minimum_array, 2))
