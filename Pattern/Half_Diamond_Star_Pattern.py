rows = int(input("Enter the number of rows for the pattern: "))

print("Hollow Half Diamond Star Pattern")

# Print the upper half of the diamond pattern
for row in range(rows):
    for column in range(row + 1):
        if row == column or column == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Print the lower half of the diamond pattern
for row in range(1, rows):
    for column in range(row, rows):
        if row == column or column == rows - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
