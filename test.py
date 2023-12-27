from  datetime import datetime

date1 = '12.05.22 12:03:25'
date2 = '12.02.23 12:03:25'


temp1 = datetime.strptime(date1, "%d.%m.%y %H:%M:%S")
temp2 =  datetime.strptime(date2, "%d.%m.%y %H:%M:%S")



print(temp1 < temp2)
