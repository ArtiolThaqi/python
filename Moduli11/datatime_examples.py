import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)
print('Year:',current_datetime.year)
print('Month:',current_datetime.month)
print('Day:',current_datetime.day)
print('Hour:',current_datetime.hour)
print('Minute:',current_datetime.minute)
print('Second:',current_datetime.second)
print('Microsecond:',current_datetime.microsecond)

#Get the current date
print("year:",current_datetime.year)
print("month:",current_datetime.month)
print("day:",current_datetime.day)

#Get the current time
current_time = datetime.datetime.now().time()

#Define a specific time
time_object = datetime.time(12,30,45,123456)
print(time_object)

print("hour:",time_object.hour)
print("minute:",time_object.minute)
print("second:",time_object.second)
print("microsecond:",time_object.microsecond)

#Get a specific date
specific_date = datetime.date(2008,3,11)
print(specific_date)

#Specific time
specific_time_object = datetime.time(12,30,45,123456)
print(specific_time_object)
