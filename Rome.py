def menu():
    choice = input("Enter 'R' for Roman numeral to decimal conversion, 'D' for decimal to Roman numeral conversion: ")
    if choice.upper() == 'R':
        n = input("Enter a Roman numeral: ")
        change_Rome_to_decimal(n)
    elif choice.upper() == 'D':
        m = int(input("Enter a decimal number: "))
        change_decimal_to_Rome(m)
    else:
        print("Invalid choice!")

def change_Rome_to_decimal(n):
    num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(n)):
        if i > 0 and num[n[i]] > num[n[i - 1]]:
            res += num[n[i]] - 2 * num[n[i - 1]]
        else:
            res += num[n[i]]
    print("Decimal value:", res)

def change_decimal_to_Rome(m):
    num = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    res = ""
    for value, symbol in num.items():
        while m >= value:
            print(value, symbol)
            res += symbol
            m -= value
    print("Roman numeral:", res)

menu()
