age=20
if age>17:
    print("your age is %s and is not an adult",%(age))
else:
    print("your age is %s and is an adult",%(age))
	
birth=int(input("Birth: "))
if birth < 2000:
	print("before 2000")
else:
	print("after 2000")
	
height = 1.75
weight = 80.5

bmi = weight/height/height
if bmi<18.5:
    print("Too light")
elif bmi <25:
    print("Normal")
elif bmi <28:
    print("Overweight")
elif bmi < 32:
    print("Fat")
else:
    print("Severely fat")