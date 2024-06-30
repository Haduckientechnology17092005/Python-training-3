print("Cac so hoan hao can tim: ")
n = 0
while True:
    condi = [1]
    [condi.append(i) for i in range(2, n) if n % i == 0]
    if sum(condi) == 2*n : print(n)
    n+=1