Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAe=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]

i=input("Enter a city name: ")
if i in Australia:
    print(f"Output: \"{i} is in Australia\"")
elif i in UAe:
    print(f"Output: \"{i} is in UAe\"")
else:
    print(f"Output: \"{i} is in India\"")        