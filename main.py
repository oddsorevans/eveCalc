# get current day and find distance from give holiday (christmas) in this case

from datetime import date

#finds the distance between 2 dates. Prints distance for testing
def dateDistance(date, holiday):
    distance = abs(date - holiday).days
    print(distance)
    return distance

#The holiday has a dummy year, since that could change depending on the current date.
#To get around that, the program finds the year of the next time the holiday will occur
#dependent on the date given
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

def main():
    #d1 can be altered to custom date to test year finding function
    d1 = date.today()
    #1 is a dummy year. Will be used to check if it is a user created year
    christmas = date(1,12,25)

    christmas = findYear(d1, christmas)

    eve = "Merry Christmas"

    #print out eve for distance. If date distance is 0, it is that day
    #and never concatenates eve
    for i in range(0, dateDistance(d1, christmas)):
        eve = eve + " eve"

    eve = eve + "!"

    print(eve)

main()