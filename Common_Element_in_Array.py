# Common Element in this 3 Arrays

array1 = [1, 2, 3, 4]
array2 = [4, 5, 2, 6]
array3 = [7, 4, 2, 8]

for i in array1:
    for j in array2:
        for k in array3:
            if i == j == k:
                print(i)
                
# Answer: 2
# Answer: 4
