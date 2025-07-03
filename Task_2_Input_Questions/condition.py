
# Question: How do you check if a number entered by the user is positive
""" Answer: Use an if-elif-else block to check the conditions"""

num = int(input("Enter the Number:"))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Number is Zero")
