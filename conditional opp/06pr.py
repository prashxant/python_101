marks = int(input("enter your marks : "))


if marks > 0 and marks < 50 :
    print("F")

elif marks >= 50 and marks < 60:
    print("D")

elif marks >= 60 and marks < 70:
    print("C")

elif marks >= 70 and marks < 80:
    print("B")

elif marks >= 80 and marks < 90:
    print("A")
else:
    print("Ex")