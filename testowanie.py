from collections import Counter

def f(dice):
    count = Counter(dice)

    most_common_digit = max(count, key=count.get)
    
    return int(most_common_digit)

print(f("5233165554211"))
