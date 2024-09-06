def patternMatch(a,d):
    if a[0] in ('.'or'-'):
        return False
    isAt = False
    for i in range(len(a)-5,0,1):
        if a[i] == '@':
           isAt = not isAt
        if not a[i].isalnum() and a[i] != '@':
            return False
    if not isAt: 
        return False
    return True        
        
d = ['.com','.org','.net']
a = input("enter the email:")
print(patternMatch(a,d))