from unicodedata import digit

multitest = """
                ______________________
               |      calculator      |
               |   ----------------   |
               |  |----------------|  |
               |   1      2      3    |
               |   4      5      6    |
               |   7      8      9    |
               |   +    -    *    /   |
               |______________________|
            """

print(multitest)
print("welcome to the calculator")

listSign = ["+", "-", "*", "/"]

number1 = input("number 1: ")
while not number1.replace('.', '', 1).isdigit():
    number1 = input("please put a number this time: ")

sign = input("operator: ")
while sign not in listSign:
    sign = input("please put an operator this time: ")

number2 = input("number 2: ")
while not number2.replace('.', '', 1).isdigit() or float(number2) == 0:
    number2 = input("please put a number this time: ")

number1 = float(number1)
number2 = float(number2)


if sign == "+":
    print(number1+number2)
elif sign == "-":
    print(number1 - number2)
elif sign == "*":
    print(number1*number2)
elif sign == "/" and number2 == 0:
    print("you cant do that")
    number2 = input("please put a number thats not zero: ")
elif sign == "/":
    print(number1/number2)
