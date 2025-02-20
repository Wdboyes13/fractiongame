import random
import sys
def gen():
	num1 = random.randrange(1, 10)
	num2 = random.randrange(1, 10)
	num3 = random.randrange(1, 10)
	num4 = random.randrange(1, 10)
	operations = ["x", "÷", "+", "-"]
	opr = operations[random.randrange(0, 3)]
	print(num1, " ", num2)
	print("-", opr, "-")
	print(num3, " ",  num4)
	return num1, num2, num3, num4, opr
num1, num2, num3, num4, opr = gen()
dec1 = num1/num3
dec2 = num2/num4
usrans1 = input("Enter your answers numerator: ")
usrans2 = input("Enter your answers denominator: ")
try:
	usrans = int(usrans1)/int(usrans2)
except:
	print("There was an error!!!")
	print("Maybe you forgot to enter a number")
	print("Please re-run program")
if opr == "x":
	ans = dec1*dec2
	print("Correct!") if usrans == ans else print("Wrong")
if opr == "+":
	ans = dec1+dec2
	print("Correct!")if usrans == ans else print("Wrong")
if opr == "-":
	ans = dec1-dec2
	print("Correct!") if usrans == ans else print("Wrong")
if opr == "÷":
	ans = dec1/dec2
	print("Correct!") if usrans == ans else print("Wrong")

