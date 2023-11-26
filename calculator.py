def switch(operator):
    if operator == "+":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        ans = round(num1 + num2, 2)
        return ans
    elif operator == "-":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        ans = round(num1 - num2, 2)
        return ans
    elif operator == "*":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        ans = round(num1 * num2, 2)
        return ans
    elif operator == "/":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        ans = round(num1 - num2, 2)
        return ans
    else:
        print("Operator not found")


op = input("Enter operator(+, -, *, /): ")
result = switch(op)
print(f"Answer: {result}")
