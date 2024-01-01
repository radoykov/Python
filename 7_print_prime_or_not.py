num = int(input('Please provide an integer:'))

if num > 1:
    k = 2
    while num % k != 0:
        k += 1
    if k == num:
        print("Number is prime")
    else:
        print("Number is not prime")
else:
    print("Number is not prime")

"""
def is_prime(num):
  if num <= 1:
    return False

  if num <= 3:
    return True
  
  if not num % 2:
    return False 

  for i in range(5, num // 2, 2):
    if not num % i:
      return False
    
  return True


N = int(input("N: "))

if is_prime(N):
  print(f"{N} is prime")
else:
  print(f"{N} is not prime")
"""
