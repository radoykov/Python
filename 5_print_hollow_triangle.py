num = int(input('Please provide triangle dimension:'))
for row in range(num):
    for j in range(num-row-1):
        print(" ", end="")
    for j in range(2*row+1):
        if j == 0 or j == 2*row:
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""
N = int(input("N: "))

for i in range(N):
  padding = " " * (N - i - 1)
  stars = "*"

  if i > 0:
    stars = "*" + " " * (i * 2 - 1) + "*"

  print(f"{padding}{stars}")

"""