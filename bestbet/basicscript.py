t1m = float(input("Enter the value of t1m: "))
t2m = float(input("Enter the value of t2m: "))
b1 = float(input("Enter the value of b1: "))
b2 = float(input("Enter the value of b2: "))

sum_val = b1 + b2 


print("1st ",  (t1m * b1 + t2m * b2) - sum_val)
print("2nd ", (t1m * b1) - sum_val)
print("3rd ", (t2m * b2) - sum_val)