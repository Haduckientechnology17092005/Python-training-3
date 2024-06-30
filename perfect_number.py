print("Print all perfect number from 1 to 10001: ")
for n in range(1, 10001):
    condi = [i for i in range (1, n+1) if n % i == 0]
    if sum(condi) == 2*n:
        print(n)