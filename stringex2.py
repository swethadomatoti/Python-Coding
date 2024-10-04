#find a count for the occurrence of a particular character in a string
s=input("Enter the string:")
x=s.count('A')
Y=s.count('B')
Z=s.count('C')
print(x,Y,Z)
#-----------------------------------------------------------------------
s=input("Enter the string:")
s=s.upper()
AC=0
BC=0
CC=0
for i in s:
    if i=='A':
        AC+=1
    elif i=='B':
        BC+=1
    else:
        CC+=1
print('count of A={}'.format(AC))
print('count of B={}'.format(BC))
print('count of C={}'.format(CC))

