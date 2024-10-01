num=int(input("enter the number:"))
n1=0
n2=1
for i in range(num):
    n=n1+n2
    n1=n2
    n2=n
    print(n1,end=' ')
