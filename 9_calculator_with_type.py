a = input('a=')
b = input('b=')
type = input('type=')
oper = input('op=')

if type == 'int':
    a = int(a)
    b = int(b)
elif type == 'float':
    a = float(a)
    b = float(b)
else:
    print('Not supported type!')

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