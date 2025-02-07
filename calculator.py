ans = []


def add():
    a1 = input("Enter 1st number:")
    if a1 == "ans":
        a1 = ans[-1]
    b1 = input("Enter 2nd number:")
    c1 = float(a1) + float(b1)
    print(f"Addition of {a1} and {b1} is {c1}")
    ans.append(c1)
    print(f"Answer stored:{ans[-1]}")


def sub():
    a2 = input("Enter 1st number:")
    if a2 == "ans":
        a2 = ans[-1]
    b2 = input("Enter 2nd number:")
    c2 = float(a2) - float(b2)
    print(f"Subtraction of {a2} and {b2} is {c2}")
    ans.append(c2)
    print(f"Answer stored:{ans[-1]}")


def mul():
    a3 = input("Enter 1st number:")
    if a3 == "ans":
        a3 = ans[-1]
    b3 = input("Enter 2nd number:")
    c3 = float(a3) * float(b3)
    print(f"Multiplication of {a3} and {b3} is {c3}")
    ans.append(c3)
    print(f"Answer stored:{ans[-1]}")


def div():
    a4 = input("Enter 1st number:")
    if a4 == "ans":
        a4 = ans[-1]
    b4 = input("Enter 2nd number:")
    c4 = float(a4) / float(b4)
    print(f"Division of {a4} and {b4} is {c4}")
    ans.append(c4)
    print(f"Answer stored:{ans[-1]}")


def power():
    a5 = input("Enter 1st number:")
    if a5 == "ans":
        a5 = ans[-1]
    b5 = input("Enter 2nd number:")
    c5 = pow(float(a5), float(b5))
    print(f"Power of {a5} to {b5} is {c5}")
    ans.append(c5)
    print(f"Answer stored:{ans[-1]}")


def mod():
    a6 = input("Enter 1st number:")
    if a6 == "ans":
        a6 = ans[-1]
    b6 = input("Enter 2nd number:")
    c6 = float(a6) % float(b6)
    print(f"Modulus of {a6} to {b6} is {c6}")
    ans.append(c6)
    print(f"Answer stored:{ans[-1]}")


def fac():
    a7 = input("Enter number:")
    if a7 == "ans":
        a7 = ans[-1]
    fact = 1
    for i in range(1, int(a7) + 1):
        fact = fact * i
    print(f"Factorial of {a7} is {fact}")
    ans.append(fact)
    print(f"Answer stored:{ans[-1]}")


print("-------SIMPLE CALCULATOR------")
print("Instructions: \n"
      "1. Enter any operator listed below \n"
      "2. To use the answer calculated just before as input, type \"ans\" \n"
      "3. Enter exit to end calculation")

while True:
    print("\n-------------------------------")
    op = input("Enter operator(+,-,*,/,^,%,!):")
    if op == '+':
        add()
    elif op == '-':
        sub()
    elif op == '*':
        mul()
    elif op == '/':
        div()
    elif op == '^':
        power()
    elif op == '%':
        mod()
    elif op == '!':
        fac()
    elif op == "exit":
        break
    else:
        print("Enter correct operator....")
