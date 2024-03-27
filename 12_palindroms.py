def pali(word):
    return word == word[::-1]
    

string = input('a = ')
words = string.split()

count = 0
longest_pal = ""
for a in words:
    if pali(a) == True:
        count +=1

        b = len(a)
        c = len(longest_pal)

        if b > c:
            longest_pal = a

print(f"Count palidromes: {count}")
print(f"The biggest palidrome: {longest_pal}")