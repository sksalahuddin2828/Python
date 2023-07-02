# A dynamic programming based on Python 
# A program for 0 - 1 knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity items

def stack_sack(items, weight, value, number):
    knapsack = [[0 for update in range(items + 1)] for update in range(number + 1)]
  
    # Build table for knapsack[][] in bottom up manner
    for first_variable in range(number + 1):
        for second_variable in range(items + 1):
            if first_variable == 0 or second_variable == 0:
                knapsack[first_variable][second_variable] = 0
            elif weight[first_variable - 1] <= second_variable:
                knapsack[first_variable][second_variable] = max(value[first_variable - 1] + knapsack[first_variable - 1][second_variable - weight[first_variable - 1]],  knapsack[first_variable - 1][second_variable])
            else:
                knapsack[first_variable][second_variable] = knapsack[first_variable - 1][second_variable]
  
    return knapsack[number][items]
  
value = [60, 100, 120]
weight = [10, 20, 30]
items = 50
number = len(value)
print(stack_sack(items, weight, value, number))


# Answer: 220
