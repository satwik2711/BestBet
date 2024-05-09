t1m = float(input("Enter the value of t1m: "))
t2m = float(input("Enter the value of t2m: "))
b1 = float(input("Enter the value of b1: "))
b2 = float(input("Enter the value of b2: "))

sum_val = b1 + b2 

print (" ")
print("best case",  (t1m * b1 + t2m * b2) - sum_val)
print("team 1 wins, team 2 no six ", (t1m * b1) - sum_val)
print("team 2 wins, team 1 no six ", (t2m * b2) - sum_val)