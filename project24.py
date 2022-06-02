# BMI Calculator.
Height=float(input("Enter Your height In CM: "))
Weight=float(input("Enter Your Weight In KG: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("Your Body Mass Index Is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("You Are Underweight")
	elif(BMI<=18.5):
		print("You Are Underweight")
	elif(BMI<=25):
		print("You Are Healthy")
	elif(BMI<=30):
		print("You Are Overweight")
	else: print("You Are Severely Overweight")
else:("Enter Valid Details")