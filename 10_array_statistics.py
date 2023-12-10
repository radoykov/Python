N = int(input('N='))
arr = []
for i in range(N):
    arr.append(int(input(f"{i+1}=")))

arr.sort()

print(f"Min value = {arr[0]}")
print(f"Max value = {arr[N-1]}")

total = 0
for element in arr:
    total += element
print(f"Average = {total/N}")

if N % 2 == 0:
    med = (arr[N//2-1]+arr[N//2]) / 2
else:
    med = arr[N//2]
print(f"Median = {med}")

ok = 0
max_num = 0
mode = -1
for i in range(N):
    ok = 0
    for j in range(i+1, N):
        if arr[j] == arr[i]:
            ok += 1
    if ok > max_num:
        max_num = ok
        mode = arr[i]

if mode == -1:
    print("No mode")
else:
    print(f"Mode = {mode}")
