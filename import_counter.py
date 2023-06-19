from collections import Counter

this_list = [10, 10, 5, 2, 9, 9, 9]
counter = Counter(this_list)

print(counter)
print(counter[10])
print(counter.most_common(1))

"""
Answer :

Counter({9: 3, 10: 2, 5: 1, 2: 1})  # count in 9 = 3 times, 10 = 2 times, 5 = 1 times, 2 = 1 times
2                                   # count 10 in 2 times
[(9, 3)]                            # common elements 9 in 3 times

"""
