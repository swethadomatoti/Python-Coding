s1=input("Enter The String:")
s1=s1.replace(" ","").lower()
s2=input("ENter the 2nd string:")
s2=s2.replace(" ","").lower()
if len(s1)==len(s2):
    n1=sorted(s1)
    n2=sorted(s2)
    if n1==n2:
        print("anagram")
    else:
        print("Not a anagram")
else:
    print("{} and {} length is not equal and it is not an anagram".format(s1,s2))