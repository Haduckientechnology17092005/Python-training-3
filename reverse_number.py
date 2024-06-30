numbers = [int(x) for x in input("Enter numbers: ").split()][::-1]
print(*[x for x in numbers if x%2!=0])