# round() : It is used to round off the digit by taking the two parameters, "round(number,no. of digit)"
'''
a=123.1234
print(round(a,1))
print(round(123.5))# it always return the nearest even integer
print(round(12.5))
print(round(13.3,0))
print(round(12.5556))
print(round(123,2))
print(round(123,0))
print(round(123,-1))# it retun the closest (10^(-no.of digits))
print(round(234,-1))
print(round(234 ,-2))
print(round(665,-1))
print(round(675,-1))
print(round(234.23,-1))
print(round(12/3,-2,))
'''
print(" ")
# WAP to calculate the year,month and days left from your total life span
age = int(input("Enter your age: "))
year_left = 90 - age
month_left = year_left * 12
days_left = year_left * 365
weeks_left = year_left * 52

print(f"You have {year_left} years and {month_left} month left {weeks_left} weeks left and {days_left} days left from your total age.")