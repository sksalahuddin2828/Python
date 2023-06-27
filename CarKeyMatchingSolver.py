from itertools import permutations

# Define the cars and keys
cars = ['R', 'B', 'G', 'Y']
keys = ['A', 'B', 'C', 'D']

# Generate all possible permutations of key-car assignments
permutations = permutations(cars)

# Check each permutation for validity
for perm in permutations:
    key_car_dict = dict(zip(keys, perm))

    # Check the given conditions
    if key_car_dict['A'] != 'B' and \
       key_car_dict['B'] != 'G' and \
       key_car_dict['C'] != 'R' and \
       key_car_dict['D'] == 'Y':
        # Valid assignment found, print the result
        print("Key-Car Assignment:")
        for key, car in key_car_dict.items():
            print(f"Key {key} is for Car {car}")
        break


#--------------------------------Math Problem--------------------------------

A car dealership has four cars for sale: a red car, a blue car, a green car, and a yellow car. The cars are parked in a row, but the dealership manager has lost the keys to the cars and doesn't know which key goes to which car. The manager has four keys, labeled A, B, C, and D. The keys are also labeled with the color of the car they belong to, but the manager has forgotten which key belongs to which car. The manager knows that:

Key A doesn't belong to the blue car.
Key B doesn't belong to the green car.
Key C doesn't belong to the red car.
Key D belongs to the yellow car.

What color is each car, and which key belongs to each car?


#--------------------------------Math Solved--------------------------------


Sure! Let's solve this using a mathematical approach.

We have four cars: a red car, a blue car, a green car, and a yellow car. We also have four keys, labeled A, B, C, and D, but we don't know which key goes with which car. We know that key A is not for the blue car, key B is not for the green car, key C is not for the red car, and key D is for the yellow car.

Let's represent the cars using variables: R for the red car, B for the blue car, G for the green car, and Y for the yellow car. We can then represent the keys that do not match each car using sets. For example, the set of keys that do not match the blue car is {A}, the set of keys that do not match the green car is {B}, and so on. We can write this as:

{A} ≠ B
{B} ≠ G
{C} ≠ R
{D} = Y

Now we need to determine which key goes with which car. Let's start with key D, which we know is for the yellow car. Therefore:

D = Y

Next, we know that key A is not for the blue car, so it must be for one of the other three cars:

A ≠ B

Similarly, we know that key B is not for the green car, so it must be for one of the other two cars:

B ≠ G

Finally, we know that key C is not for the red car, so it must be for the remaining car:

C ≠ R

Putting it all together, we get:

A = G or A = R or A = Y
B = R or B = Y
C = B or C = G or C = Y
D = Y

But we also know that each key matches only one car, so we can use this information to narrow down the possibilities. For example, if key A matches the green car, then we have:

A = G, B = Y, C = B or C = Y, D = Y

This means that the red car and the green car cannot both match keys A and C, because then both keys would match the yellow car. Therefore, key A must match either the red car or the yellow car, and key C must match the remaining car.

We can repeat this process for the other possibilities of key A, and we will find that the only valid solution is:

A = R, B = Y, C = G, D = Y

Therefore, the red car matches key A, the blue car matches key B, the green car matches key C, and the yellow car matches key D.
