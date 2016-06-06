# Emily Wheelock-Davis                              Feb 2014
# DayOfYear_gui.py
#
# Opens a gui that allows user to do one of two things:
# 1. Enter a date, hit calculate, and receive the day of the year
# 2. Enter day of the year, hit calculate, and receive the date

from Tkinter import *

#END_PROGRAM = 3
MONTHS = ['January','February','March','April','May','June',\
          'July','August','September','October','November','December']
        

#returns true if parameter is a leap year, false otherwise
def IsLeapYear(yr):
    if yr%100 == 0:
        if yr%400 == 0:
            return True
        else:
            return False
    elif yr%4 == 0:
        return True
    else:
        return False


def getMonthNum(m):
    for month in range(0,11):
        if MONTHS[month] == m:
            return month+1


# Get date from day of year
def GetDate():
    year = int(y.get())

    if IsLeapYear(year):
        #days in each month for leap year:
        yearDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        #days in each month for non-leap year:
        yearDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dayOfYr = int(o.get())
    currentMonth = 1    #iterates up to month
    totalDays = dayOfYr     #iterates down to day

    # Find month in which doy (day of year) falls:
    while totalDays > yearDays[currentMonth-1]:
        totalDays = totalDays - yearDays[currentMonth-1]
        currentMonth = currentMonth + 1
    day = totalDays
    d.set(day)
    v2.set(MONTHS[currentMonth-1])
   

# Get day of the year from date
def GetDayOfYear():
    year = int(y.get())
    if IsLeapYear(year):
        yearDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        yearDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = v2.get()
    monthNum = getMonthNum(month)
    day = int(d.get())
    if day > yearDays[monthNum-1]:
        e.set("Too many days in the month! Try again!")
        return
    
    prevMonth = 1
    doy = 0
    while prevMonth < monthNum:
        doy = doy + yearDays[prevMonth-1]
        prevMonth = prevMonth + 1
    doy = doy + day

    o.set(doy)



#Button Calculate function:
def CalcNow():
    e2 = d.get()
    e3 = y.get()
    e4 = o.get()
    if e3 == "":
        e.set("Must have a year! Please enter one!")
        return
    if e2 != "" and e4 != "":
        e.set("You cannot enter both Date and Day of Year! Choose only one!")
        return
    if (e2 == "" or e2 == "0") and (e4 == "" or e4 == "0"):
        e.set("Please enter a Date or a Day of Year!")
        return
    if e2 != "":
        e.set("")
        GetDayOfYear()
    elif e2 == "":
        e.set("")
        GetDate()


def ClearAll():
    v2.set(MONTHS[0])
    d.set("")
    y.set("")
    o.set("")
    e.set("")


if __name__ == "__main__":

    root = Tk()         # initialize Tk object
    root.geometry("490x150+300+300")
    root.title("Enter Date or Day of Year")

    v2 = StringVar(root)
    v2.set(MONTHS[0])
    d = StringVar(root)
    y = StringVar(root)
    o = StringVar(root)
    e = StringVar(root)
    e.set("Enter Year and either Day of Year or Date")

    dateLabel = Label(root, text="Date:").grid(column=1, row=1)
    optMonth = OptionMenu(root, v2, MONTHS[0], MONTHS[1],\
                          MONTHS[2], MONTHS[3], MONTHS[4], MONTHS[5],\
                          MONTHS[6], MONTHS[7], MONTHS[8], MONTHS[9],\
                          MONTHS[10], MONTHS[11]).grid(column=2, row=1)

    e2day = Entry(root, textvariable=d).grid(column=3, row=1)
    yrLabel = Label(root, text="Year:").grid(column=5, row=1)
    e3yr = Entry(root, textvariable=y).grid(column=5, row=2)
    doyLabel = Label(root, text="Day of Year:").grid(column=1,row=3)
    e4doy = Entry(root, textvariable=o).grid(column=2, row=3)
    errLabel = Label(root, textvariable=e, fg="red")\
               .grid(column=1, columnspan=5, row=4)
    button1 = Button(root, text="Calculate",command=CalcNow)\
              .grid(column=2, row=5)
    button2 = Button(root, text="Clear",command=ClearAll)\
              .grid(column=4, row=5)
    root.mainloop()

