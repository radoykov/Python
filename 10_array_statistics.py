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

"""
N = int(input("N: "))
num_list = []

if N < 2:
  raise Exception("N cannot be lower than 2")

for i in range(N):
  new_num = int(input(f"{i+1}: "))
  num_list.append(new_num)

def get_average(list):
  sum = 0

  for num in list:
    sum += num

  return sum / len(list)

def get_min_max(list):
  list_copy = [*list]

  list_copy.sort()

  return (list_copy[0], list_copy[-1])

def get_mode(num_list):
  list_copy = [*num_list]

  num_occurences = {}

  for num in list_copy:
    if not num in num_occurences.keys():
      num_occurences.update({num: num_list.count(num)})
    
  max = list(num_occurences.keys())[0]

  for item in list(num_occurences.items())[1:]:
    if num_occurences[max] < item[1]:
      max = item[0]

  if num_occurences[max] == 1:
    return None
  return max

def get_median(num_list):
  list_copy = [*num_list]
  list_copy.sort()

  median_index = (len(list_copy)-1)//2

  if len(list_copy) % 2:
    return list_copy[median_index]
  return (list_copy[median_index] + list_copy[median_index+1])/2



print(f"(Min, Max): {get_min_max(num_list)}")
print(f"Average: {get_average(num_list)}")
print(f"Mode: {get_mode(num_list)}")
print(f"Median: {get_median(num_list)}")
"""