rows = int(input("Enter the number of rows for the pattern: "))

print("Full Diamond Star Pattern")

# Print the upper half of the diamond pattern
for row in range(rows):
    for column in range(rows - row - 1):
        print(' ', end='')
    for column in range(row + 1):
        print('*', end=' ')
    print()

# Print the lower half of the diamond pattern
for row in range(rows - 1, 0, -1):
    for column in range(rows - row):
        print(' ', end='')
    for column in range(row):
        print('*', end=' ')
    print()
