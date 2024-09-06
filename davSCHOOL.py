arr = [0]*101
for i in range(1,8):
    for k in range(1,101):
        if(k%i==0):
            if(arr[k]==0):
                arr[k]=1
            else:
                arr[k]=0
        k+=1
    i+=1
close=0
open=0
for i in range(100):
    if(arr[i]==0):
        close+=1
    else:
        open+=1
print("DOORS OPENED :",open)
print("DOORS CLOSED :",close)