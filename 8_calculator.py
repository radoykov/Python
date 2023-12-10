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