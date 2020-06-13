import calendar
y = int(input("Input the year: "))
m = int(input("Input the month in number terms: "))
print(calendar.month(y, m))

print("Hint: We have 'import calendar' at the top of the code \n with y=... and m=... in the middle \n and then at the end, we have 'calendar.month' \n in order to tell python how to know which month, and not just print a number with the year beside it")
