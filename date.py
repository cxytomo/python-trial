months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
daySuffix = ["st","nd","rd"] + ["th"]*17 + ["st","nd","rd"] + ["th"]*7 + ["st"]
year = raw_input("Year:")
month = input("Month:")
day = input("Day(1-31):")
print months[month-1] + " " + repr(day) + daySuffix[day-1] + ". " + year