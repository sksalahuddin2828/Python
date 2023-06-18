import timeit

def while_loop(n = 100000000):
  i = 0
  s = 0
  while i < n:
    s += 1
    i += 1
  return 0

def for_loop(n = 100000000):
  s = 0
  for i in range(n):
      s += 1
  return 0

def main():
  print("while_loop\t\t", timeit.timeit(while_loop, number=1))
  print("for_loop\t\t", timeit.timeit(for_loop, number=1))
  
if __name__ == '__main__':
  main() 
