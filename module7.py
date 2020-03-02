import sys
import datetime

data = datetime.datetime.now().time()
print(data)


from datetime import timedelta
from datetime import datetime
print (datetime.now() - timedelta(seconds=60) + timedelta(days=730))


d = timedelta(days = 100, hours = 10, minutes = 13)
(d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)

print(d)