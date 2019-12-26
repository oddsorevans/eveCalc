# get current day and find distance from give holiday (christmas) in this case

from datetime import date

def dateDistance(date, holiday):
    distance = abs(date - holiday).days
    print(distance)
    return distance

def findYear(date, holiday):
    if date.month < holiday.month:
        holiday = holiday.replace(date.year)
    elif date.month > holiday.month:
        holiday = holiday.replace(date.year + 1)
    else:
        if date.day > holiday.day:
            holiday = holiday.replace(date.year + 1)
        else:
            holiday = holiday.replace(date.year) 
    return holiday


d1 = date(2019,12,24)
christmas = date(1,12,25)

christmas = findYear(d1, christmas)

eve = "Merry Christmas"

for i in range(0, dateDistance(d1, christmas)):
    eve = eve + " eve"

eve = eve + "!"

print(eve)