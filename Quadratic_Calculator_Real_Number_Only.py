import math

#(-b + sqrt(b^2 - 4AC))/2a
print("Welcome to the Quadratic Formula Calculator")
print("In the format ax^2 + bx + c = 0")   
A = eval(raw_input("What is the Value of A?"))
B = eval(raw_input("What is the Value of B?"))
C = eval(raw_input("What is the Value of C?"))

D = B**2-4*A*C # discriminant

if D < 0:
    print ("This equation has no real solution")
elif D == 0:
    x1 = (-B+math.sqrt(B**2-4*A*C))/2*A
    print ("This equation has one solutions: "), x1
else:
    x1 = (-B+math.sqrt((B**2)-(4*(A*C))))/(2*A)
    x2 = (-B-math.sqrt((B**2)-(4*(A*C))))/(2*A)
    print ("This equation has two solutions: ", x1, " or", x2)
