a=13
print(a)
while True:
    if a % 2 != 0:
        a = a + 1
    else:
        a = a // 2
    print(a)
    if a == 1:
        break
