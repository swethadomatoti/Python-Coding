#write a program to calculate number of vowels and consonants
#s='swetha'
#count(s)--cal of vowels
#count(s)--cal of consonants
s=input("Enter the string:")
vowels=['a','e','i','o','u','A','E','I','O','U']
vc=0
cc=0
for i in s:
    if i in vowels:
        vc+=1
    else:
        cc+=1
print('{} vowels are there in given string'.format(vc))
print('{} consonants are there in given string'.format(cc))
