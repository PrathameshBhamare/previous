# Program to display calendar of the given month and year

# importing calendar module
import calendar
#below enter year and month to see the calender for example the year is 2014 and month is 11

yy = 2022  # year
mm = 4    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))