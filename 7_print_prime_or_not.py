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


