#find the count of all odd and even no is multiplication table between 3 and 7
def func(n1,n2):
    if n1<n2:
        min = n1 
        max = n2
    else:
        min = n2
        max = n1
    odd = 0
    even = 0
    for i in range(min,max+1):
        for j in range(1,11):
            temp=i*j
            if temp&1:
                odd+=1
            else:
                even+=1
    return f'no of odds: {odd} and no of even: {even}'       
        
        
n1 = int(input("enter the number 1:"))
n2 = int(input("enter the number 2:"))
print(func(n1,n2))