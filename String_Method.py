# startswith()
# endswith()

string = "Python"

print(string.startswith("Py"))
print(string.endswith("on"))

string = "Hmm, I don't know"
fillers = ("Well", "Hmm", "Um", "Like")
print(string.startswith(fillers))

string = "Hey!"
punctuations = (".", "?", "!")
print(string.endswith(punctuations))

# Answer: True
