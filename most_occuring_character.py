from collections import Counter

def find_most_occ_char(string):
    # Create a dictionary using Counter method
    # which will have characters as keys and their
    # frequencies as values
    char_count = Counter(string)

    # Finding the maximum occurrence of a character
    # and getting its count and character
    max_count = max(char_count.values())
    most_occ_char = [char for char, count in char_count.items() if count == max_count]

    # Printing the most occurring character(s) and its count
    for char in most_occ_char:
        print(f"Character: {char}, Count: {max_count}")

# Driver program
if __name__ == "__main__":
    input_string = 'helloworldmylovelypython'
    find_most_occ_char(input_string)


# Answer: Character: l, Count: 5
