N=int(input('N='))
v=N
b=0
while N!=0:
    b+=1
    N=N//10
N=v
b=b//2

x=5*10**(b-1)
f=x
for i in range(3):
    a=(N-f**2)/(2*f)
    b=f+a
    f=b-((a**2)/(2*b))
print(f)
l=x
for i in range(5):
    l=(1/3)*(2*l+(N/(l**2)))
print(l)

"""
from math import sqrt


def calc_bashkhali_number(original, guess):
    a = (original - guess ** 2)/(2*guess)
    b = guess + a
    return b - ((a ** 2)/(2*b))


def cube_root(original, guess):
    return (1/3) * ((2*guess) + (original/(guess**2)))


def square_root(num, func, duration):
    guess = 5 * 10 ** (len(str(num))//2 - 1)

    if num < 10:
        guess = num / 2

    for _ in range(duration):
        print(guess)
        guess = func(num, guess)

    return guess


N = int(input("N: "))

print(square_root(N, calc_bashkhali_number, 4))
print(square_root(N, cube_root, 4))
print(sqrt(N))
"""