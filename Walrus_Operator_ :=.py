# Before using Walrus Operator :=

if __name__ == '__main__':
    
    sentence = "This is a very long sentence or heavy."
    
    words = sentence.split()
    
    information = {
        "words": words
    }
    
    print(information)
    
# Answer: {'words': ['This', 'is', 'a', 'very', 'long', 'sentence', 'or', 'heavy.']}

#--------------------------------------------------------------------------------------------

# After using Walrus Operator :=

if __name__ == '__main__':
    
    sentence = "This is a very long sentence or heavy."
    
    information = {
        "words": (words := sentence.split())
    }
    
    print(information)
    
# Answer: {'words': ['This', 'is', 'a', 'very', 'long', 'sentence', 'or', 'heavy.']}

#---------------------------------Real power of Walrus Operator := --------------------------------

# Walrus Operator :=

if __name__ == '__main__':
    
    sentence = "This is a very long sentence or heavy."
    
    information = {
        "words": (word := sentence.split()),
        "charecter": (char := len(''.join(word)))
    }
    
    print(information)
      
# Answer: {'words': ['This', 'is', 'a', 'very', 'long', 'sentence', 'or', 'heavy.'], 'charecter': 31}

#--------------------------------------------------------------------------------------------

# Walrus Operator :=

if __name__ == '__main__':
    
    sentence = "This is a very long sentence or heavy."
    
    information = {
        "words": (word := sentence.split()),
        "charecter": (char := len(''.join(word))),
        "average_charecter_per_word": round(char / len(word) ,2)
    }
    
    print(information)
    
# Answer: {'words': ['This', 'is', 'a', 'very', 'long', 'sentence', 'or', 'heavy.'], 'charecter': 31, 'average_charecter_per_word': 3.88}

#-----------------------------------------------------------------------------------------------------------------------------------------

# Walrus Operator :=
# it's return True

if __name__ == '__main__':
    
    name = "Sk. Salahuddin"
    empty_name = ""
    
    if temp_name := empty_name or name:
        print(temp_name)
        print("Executed")
        
# Answer: Sk. Salahuddin
#          Executed

#-----------------------------------------------------------------------------------------------------------------------------------------

# Walrus Operator :=
# if both are empty it's return False

if __name__ == '__main__':
    
    name = ""
    empty_name = ""
    
    if temp_name := empty_name or name:
        print(temp_name)
        print("Executed")
        
 #-----------------------------------------------------------------------------------------------------------------------------------------
 
# Walrus Operator :=
# if any value find two this variable it return True

if __name__ == '__main__':
    
    name = ""
    empty_name = "Empty"
    
    if temp_name := empty_name or name:
        print(temp_name)
        print("Executed")
        
# Answer: Empty
#         Executed
