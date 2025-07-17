import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)
if hour > 0 and hour < 12:
    print("Good Morning sir")
elif hour > 0 and hour < 12:
    print("Good Afternoon sir!")   
else:
    print("Good Evening sir!") 

