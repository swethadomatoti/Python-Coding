num=int(input("enter th number:"))
arm=[]
not_arm=[]
for i in range(num+1):
    n = len(str(i))
    sum = 0
    temp = i
    while temp>0:
        digit=temp%10
        sum+=digit**n
        temp//=10
    if i==sum:
        arm.append(i)
    else:
        not_arm.append(i)
print("{} all are the armstrong numbers".format(arm))
print("{} all are the not a armstrong numbers".format(not_arm))


