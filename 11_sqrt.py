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