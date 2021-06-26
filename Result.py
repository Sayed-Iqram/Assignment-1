print("what kind of result do you want to? ")
print("Choose 1- Grade Marking")
print("Choose 2- Number Marking")


class Chossen:
    pass


int(input("Enter Your Chose\n"))

if int: str = "1"

grade = float(input('Enter Your Grade: '))
if grade == 4:
    print("A+")
elif 3.75 <= grade <= 3.99:
    print("A")
elif 3.26 <= grade <= 3.74:
    print("A-")
elif 3.1 <= grade <= 3.25:
    print("B+")
elif 2.76 <= grade <= 3:
    print("B")
elif 2.51 <= grade <= 2.75:
    print("b-")
elif 2.1 <= grade <= 2.5:
    print("C+")
elif grade == 2:
    print("C")
elif grade < 2:
    print("fail")
else:
    print("invalid Grade")


if int: str = "2"

mark = int(input("Enter Marks:"))

if 80 <= mark <= 100:
    print("A+")
elif 75 <= mark <= 79:
    print("A")
elif 70 <= mark <= 74:
    print("A-")
elif 65 <= mark <= 69:
    print("B+")
elif 60 <= mark <= 64:
    print("B")
elif 55 <= mark <= 59:
    print("B-")
elif 50 <= mark <= 54:
    print("C+")
elif 45 <= mark <= 49:
    print("C-")
elif 40 <= mark <= 44:
    print("D")
elif 0 <= mark <= 39:
    print("F")
else:
    print("Invalid Mark")
