n = int(input())
A = []
words = []

for i in range(0,n):
    r = str(input())
    relmin = ord("z")
    for j in r:
        if j=="a":
            relmin = ord(j)
            break
        elif ord(j)<relmin:
            relmin = ord(j)

    words.append(chr(relmin))

words.sort()

w = ""

for i in words:
    w += i

print(w)
