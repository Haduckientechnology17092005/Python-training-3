a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print("UCLN của hai số là: ", end="")
while a!=b:
    if a>b:
        a = a-b
    else:
        b = b-a
print(a)