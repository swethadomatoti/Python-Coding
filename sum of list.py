#ad the elements in list without using built-in functon
#l=[2,4,4]=10
#---------------------------------------------------------------\
#using built in function
#l=[2,4,4]
#print(sum(l))
#----------------------------------------------------------------
def sum_list(x):
    sum=0
    for i in x:
        sum+=i
    return sum
y=sum_list([2,4,4])
print(y)
