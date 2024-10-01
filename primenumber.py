num=int(input("Enter the Number:"))
prime_number=[]
not_prime=[]
for i in range(2,num+1):
    for j in range(2,i):
        if i%j==0:
            not_prime.append(i)
            break
    else:
        prime_number.append(i)
print(not_prime)
print(prime_number)


