"""
for loop
"""
#for loop
x = 0
for x in range(0, 10):
    print(x)

# #continue
i = 0
for i in range(0, 10):
    if i == 5:
        continue
    print(i)

#break
j = 0
for j in range(0, 10):
    print(j)
    if j == 5:
        break

"""
while loop
"""
a = 1

while a <= 5:
    print(a)
    a += 1

b = 5

while b >= 1:
    print(b)
    b -= 1

c = 1

while c <= 5:
    print(c)
    if c == 3:
        break
    c += 1

d = 0

while d <= 5:
    d += 1
    if d == 3:
        continue
    print(d)