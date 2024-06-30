import math
n = int(input("Enter a number: "))
def sum_container(n):
    sum = 0 
    for i in range(1, n+1):
        sum = sum + 1/i
    print(sum)
    
def sum_geometry(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + 1/(i**2)
    print(sum)

def sum_conductor(n):
    sum = 0
    dau = 1
    for i in range(1, n+1):
        sum = sum + (1/i)*dau
        dau = -dau
    print(sum)
    
def sum_math(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + 1/(i*(i+1))
    print(sum)

def sum_math2(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + math.sqrt(i)
    print(sum)
    
def exp_x(x):
    eps = 0.0001
    sum = 1
    i = 1
    t = 1
    while abs(t) >= eps:
        t = t*(x/i)
        sum = sum + t
        i = i + 1
    print(sum)

def sin_x(x):
    eps = 0.0001
    sum = x
    i = 1
    t = x
    dau = -1
    while abs(t) >= eps:
        t = t*(x**2)/(2*i*(2*i+1))
        sum = sum + t*dau
        dau = -dau
        i = i + 1
    print(sum)

def cos_x(x):
    eps = 0.0001
    sum = 1
    i = 1
    t = 1
    dau = -1
    while abs(t) >= eps:
        t = t*(x**2)/(2*i*(2*i-1))
        sum = sum + t*dau
        dau = -dau
        i = i + 1
    print(sum)

def menu(n):
    sum_container(n)
    sum_geometry(n)
    sum_conductor(n)
    sum_math(n)
    sum_math2(n)
    exp_x(1)
    sin_x(3.14)
    cos_x(3.14)

menu(n)