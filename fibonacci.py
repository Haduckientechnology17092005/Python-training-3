def fibonacci():
    i=1
    f1=1
    f2=1
    n=int(input("Enter number: "))
    print("Day Fibonacci can tim voi do dai: ",n,"cho truoc gom cac so khac 0 la: ")
    fi = f1+f2
    print(f1,f2,end=" ")
    print(fi, end=" ")
    for i in range (3,n):
        f1=f2
        f2=fi
        fi=f1+f2
        print(fi, end=" ")

fibonacci()