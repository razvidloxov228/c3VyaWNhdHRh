import calculator
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /): ")
if operation == "+":
    result = calculator.add(a, b)
elif operation == "-":
    result = calculator.subtract(a, b)
elif operation == "*":
    result = calculator.multiply(a, b)
elif operation == "/":
    result = calculator.divide(a, b)
else:
    result = "Невідома операція!"
print("Результат:", result)