# Powerful Python Snippet of Code

def today(lst: list, n: int):
  for i in range(0, len(lst), n):
    yield lst [i:i + n]

sample: list[str] = ['a', 'b', 'c', 'd', 'e']

print(sample)
print("")
print(list(today(sample, 2)))
print("")
print(list(today(sample, 3)))

