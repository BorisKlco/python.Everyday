"""
Bubble sort

take bubble[n] 
compere it with bubble[n+1]
if bigger, than swap
otherwise n +=1
"""
bubble = [2, 1, 7, 5, 6, 9, 8, 3, 4]
print(bubble)

for n in range(len(bubble) - 1):
    for n in range(len(bubble) - 1):
        if bubble[n] > bubble[n + 1]:
            value_holder = bubble[n]
            bubble[n] = bubble[n + 1]
            bubble[n + 1] = value_holder


print(bubble)
