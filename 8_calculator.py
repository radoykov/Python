a = int(input('a='))
b = int(input('b='))
oper = input('op=')

if oper == 'add':
    print(f"res:{a+b}")

elif oper == 'substract':
    print(f"res:{a - b}")

elif oper == 'multiply':
    print(f"res:{a * b}")

elif oper == 'divide' and b != 0:
    print(f"res:{a / b}")

elif oper == 'power':
    print(f"res:{a ** b}")

else :
    print('Not supported operation!')

"""
def operation(operation, a, b):
    if operation == "+":
        result = a + b

    elif operation == "-":
        result = a - b

    elif operation == "*":
        result = a * b

    elif operation == "/":
        if b == 0:
            raise Exception("B cannot be zero")
        result = a / b

    elif operation == "**":
        result = a ** b

    else:
        raise Exception(f"Operation {operation} not supported")

    return float(format(result, ".3f"))


a = float(input("a: "))
b = float(input("b: "))
operation_str = input("operation: ")

print(operation(operation_str, a, b))
"""