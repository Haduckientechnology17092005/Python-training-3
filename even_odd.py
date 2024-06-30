giatri = input("Nhap day so vao, cac so cach nhau boi dau phay: ")
so = [x for x in giatri.split(",") if int(x)%2!=0]
print("Day chi toan so le: ",",".join(so))