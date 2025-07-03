#  4. Question: How you can take multiple space-separtated value as input() 
"""Answer: You can use `split()` to split the input string into a list of values: """

values = input("Enter values: ").split()
print(values)

# Take space seprate integers
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# Tking float
numbers = list(map(float, input("Enter the numbers: ").split()))
print(numbers)
