def isphonenumber(numstr):
    if len(numStr) != 12:
        return False 
    for i in range(len(numstr)):
        if i == 3 or i == 7:
            if numstr[i] != "-":
                return False
            else:
                if numstr[i].isdigit() == false:
                    return False
    return True
def chkphonenumber(numstr):
    ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match(numstr):
        return True
    else:
        return False    
ph_num = input("enter a phone number:")   