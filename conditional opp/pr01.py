
a = int(input("enter your number: "))
b = int(input("enter your number: "))
c = int(input("enter your number: "))
d = int(input("enter your number: "))

if a >= b and a >= c and a >= d:
    print(f"The greatest number is {a}")
elif b >= a and b >= c and b >= d:
    print(f"The greatest number is {b}")
elif c >= a and c >= b and c >= d:
    print(f"The greatest number is {c}")
else:
    print(f"The greatest number is {d}")
