# Population growth function
def population_growth(t):
    initial_population = 4000
    growth_rate = 1000
    population = initial_population + growth_rate * t
    return population

# Calculate population after 1 hour
population_after_1_hour = population_growth(1)
print("Population after 1 hour:", population_after_1_hour)


# Answer: Population after 1 hour: 5000
