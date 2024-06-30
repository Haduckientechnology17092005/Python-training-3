n = int(input("Enter number n>0: "))
sum = 0.00
for i in range(1,n+1):
    sum = sum + float(float(i)/(i+1))
print(sum)