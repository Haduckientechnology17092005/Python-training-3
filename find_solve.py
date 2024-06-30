def menu():
    n = int(input("Enter a number: "))
    solve(n)

def solve(n):
    for x in range (0,51):
        for y in range (0,51):
            if (x**2 + y**2 == n):
                print("(",x,",",y,")")

menu()