val = int(input("enter a value :"))
str_val = str(val)
if str_val == str_val[::-1]: # check if the string is palindrome or not
    print("palindrome")
else:
    print("not palindrome")
    
for i in range(10):
    if str_val.count(str(i)) > 0 :
        print(str(i),"appears",str_val.count(str(i)),"times");