print("Bang cac so nguyen to nho hown 500: ")
for num in range (1, 501):
    if num==2:
        print(num)
    else:
        for i in range (2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
                break
        