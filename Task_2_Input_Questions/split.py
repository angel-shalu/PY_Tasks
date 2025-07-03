
# Question: How you can take multiple space-separtated value as input() 
"""Answer: You can use `split()` to split the input string into a list of values: """

values = input("Enter values: ").split()
print(values)

# Take space seprate integers
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# Tking float
numbers = list(map(float, input("Enter the numbers: ").split()))
print(numbers)





# Question: How do u convert user input to a list of integers 
"""Answer: After using split(), you can convert each element to an integer using a 
list comprehension: """

num = [int(x)for x in input("Enter the numbers :").split()]

# Here Printing the list
num = [int(x)for x in input("Enter the numbers :").split()]
print(num)


