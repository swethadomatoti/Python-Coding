num=int(input("enter the number:"))
even_num=[]
odd_num=[]
if num==0:
    print("{} invalid input please enter above ZERO numbers".format(num))
for i in range(1,num+1):
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print('{} all are even numbers'.format(even_num))
print('{} all are odd numbers'.format(odd_num))
