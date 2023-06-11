def analyse_text(text: str) -> dict:
    # words = text.split()
    
    details: dict = {
        'words': (words := text.split()),
        'amount': len(words),
        'chars': len(''.join(words)),
        'reversed': words[::-1]
    }
    
    return details

print(analyse_text('Hello world'))

# Answer: {'words': ['Hello', 'world'], 'amount': 2, 'chars': 10, 'reversed': ['world', 'Hello']}

#-----------------------------------------------------------------------------------------------------

user_input: str = 'Hello world!'

# text = len(user_input)

if (text := len(user_input) > 5):
    print(text, '👍')
else:
    print(text, '👎')
    
# Answer: True 👍

#-----------------------------------------------------------------------------------------------------

def get_value():
    return None
    
# var = get_value()

if var := get_value():
    print(var)
else:
    print('No value!')
    
# Answer: No value!
