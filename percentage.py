tyle = 0.003
nam = 2020
danso = 96525000
while danso<=1e8:
    nam += 1
    danso *= (1+tyle)
    print(nam, danso)
print("Som nhat den nam: ", nam)