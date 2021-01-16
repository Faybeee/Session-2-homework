#Write a program which will ask for two numbers from a user.
#Then offer a menu to the user giving them a choice of maths operators.
#Once the user has selected which operator they wish to use,
# perform the calculation by using a procedure and passing parameters.

def procedure_a(first,second):
    print(first + second)

def procedure_b(first,second):
    print(first-second)

def procedure_c(first,second):
    print(second / first)

def procedure_d(first, second):
    print(second*first)

def procedure_e(first, second):
    print(first ** second)

def procedure_f(first, second):
    print(pow(first, 2), pow(second, 2))

print("Hi! I'm here to help you calculate! I want you to give me two numbers!")
first = int(input("What is your first number choice?"))
second = int(input("What is your second number choice?"))
print("Great job!")

print ("""
    A = Add Numbers together.
    B = Subtract the second number from the first.
    C = Divide second number by first number.
    D = Multiply numbers together.
    E = First number to the power of second.
    F = Square the numbers.
    """)
method = str(input("Choose a letter A-F"))

if method == "A" or method =="a":
    procedure_a(first,second)

elif method == "B" or method =="b":
    procedure_b(first,second)

elif method == "C" or method =="c":
    procedure_c(first, second)

elif method == "D" or method =="d":
    procedure_d(first, second)

elif method == "E" or method =="e":
    procedure_e(first, second)

elif method == "F" or method =="f":
    procedure_f(first, second)