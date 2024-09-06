from datetime import datetime
s1 = datetime(2021,12,3)
s2 = datetime(2024,12,3)
dif = (s2.year - s1.year)*365
diff = ((s2.year - s1.year)*12 +(s2.month-s1.month))*30
di = s2.day-s1.day
difference = dif+diff+di
print(difference)