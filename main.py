# get current day and find distance from give holiday (christmas) in this case

from datetime import date

def dateDistance(date, holiday):
    return abs(date - holiday).days

d1 = date(2019,12,30)
christmas = date(2019,12,25)

eve = "Merry Christmas"

for i in range(0, dateDistance(d1, christmas)):
    eve = eve + " eve"

eve = eve + "!"

print(eve)