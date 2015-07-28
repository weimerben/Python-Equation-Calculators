import math
print("Given the length of two sides I can calculate the length of the third")
A = eval(raw_input("What is the length of the first side?"))
B = eval(raw_input("What is the length of the second side?"))
C = math.sqrt( (A ** 2) + (B ** 2))
print('The Length of the third side is...')
print C
