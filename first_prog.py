import time
print("time is : " + str(time))
now = time.localtime()
print("now : " + str(now))
hour = now.tm_hour
print(hour)

correction = input("give correction ")
print("correction given : " + str(correction))

if hour < 8: print('sleeping')
elif hour < 9: print('commuting')
elif hour < 17: print('working')
elif hour < 18: print('commuting')
elif hour < 20: print('eating')
elif hour < 22: print('resting')
else: print('sleeping')

aantal = int(input("hoeveel lijnen wil je: "))
for j in range(1, aantal):
    print(j)
