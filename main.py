#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print(" Welcome to tip calculator\n")
total_bill= float(input("How much was the bill  $"))
tip_percent = float(input("How many percent tip do you want to give? 10, 12 or 15\n"))
total_amount = (1+tip_percent/100)*total_bill
number_persons = int(input("among how many people is the bill shared\n"))
uni_amount = round(total_amount/number_persons,2)                                                                                                                                                                                       
print(f"Each person will be expected to contribute {uni_amount} $")
