from math import comb

# Calculate the total number of possible hands
total_hands = comb(52, 5)

# Calculate the number of three-of-a-kind hands
three_of_a_kind_hands = 13 * comb(4, 3) * comb(12, 2) * comb(4, 1) * comb(4, 1)

# Calculate the probability of getting a three-of-a-kind hand
probability_three_of_a_kind = three_of_a_kind_hands / total_hands
print("Probability of getting a three-of-a-kind poker hand:", probability_three_of_a_kind)


# Answer: Probability of getting a three-of-a-kind poker hand: 0.02112845138055222
