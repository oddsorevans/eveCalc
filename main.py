# get current day and find distance from give holiday (christmas) in this case

from datetime import date
import json

#made a global to be used in functions
holidayList = []

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

#check if a given variable is in the list, and return true or false
def findInList(list, variable):
    present = False
    for i in list:
        if i == variable:
            present = True
    return present

#get user input
def userInput():
    desired = input("What holiday would you like to calculate the eve for? Type options for available holidays\n")
    #keep window open until they get the correct answer
    correctInput = False
    while correctInput ==  False:
        if desired == "options":
            print(holidayList)
            desired = input("What holiday would you like to calculate the eve for? Type options for available holidays\n")
        else:
            if findInList(holidayList, desired) == True:
                correctInput = True
            else: 
                print("That is not a valid holiday")
                desired = input("What holiday would you like to calculate the eve for? Type options for available holidays\n")
    return desired

def main():
    #take contents of json and load into dictionary
    holidayDict = {}
    scratch = open("holidays.json", 'r')
    temp = scratch.read()
    holidayDict = (json.loads(temp))
    #create list with all the titles so that the user knows input options
    #as well as something to check their input on
    for i in holidayDict["holidayList"]:
        holidayList.append(i)

    desired = userInput()

    print(holidayDict["holidayList"][desired])
    #d1 can be altered to custom date to test year finding function
    d1 = date.today()
    #1 is a dummy year. Will be used to check if it is a user created year
    holiday = date(holidayDict["holidayList"][desired]["year"],holidayDict["holidayList"][desired]["month"],holidayDict["holidayList"][desired]["day"])

    holiday = findYear(d1, holiday)

    eve = "Merry " + desired

    #print out eve for distance. If date distance is 0, it is that day
    #and never concatenates eve
    for i in range(0, dateDistance(d1, holiday)):
        eve = eve + " eve"

    eve = eve + "!"

    print(eve)

main()