h=float(input("Enter height in meters: "))
w=float(input("Enter weight in kilograms: "))

bmi=w/(h*h)

if bmi>=30:
    print("Output: \"Obesity\"")
elif 25<bmi<29:
    print("Output: \"Overweight\"")
elif 18.5<bmi<25:
    print("Output: \"Normal\"")
elif bmi<18.5:
    print("Output: \"Underweight\"")    