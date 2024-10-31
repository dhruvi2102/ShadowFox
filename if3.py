Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

i = input("Enter the first city: ")
j = input("Enter the second city: ")

if i in Australia and j in Australia:
    print("Output: \"Both cities are in Australia\"")
elif i in UAE and j in UAE:
    print("Output: \"Both cities are in UAE\"")
elif i in India and j in India:
    print("Output: \"Both cities are in India\"")
else:
    print("Output: \"They don't belong to the same country\"")
