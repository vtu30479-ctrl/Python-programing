import datetime

input_date = input("Enter the date in MM DD YYYY format: ")
month, day, year = map(int, input_date.split())

if 2000 < year < 3000:
    x = datetime.datetime(year, month, day) 
    day_name = x.strftime("%A").upper() 
    print(day_name)
else:
    print("Year is not within the specified constraints.")
