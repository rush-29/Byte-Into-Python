# We use "def" to define a function.
# This sum function takes two parameters, a and b. 
def sum_two_values(a, b):
    return a + b
    
# create two variables and assign integer values to them: 
first = 2 
second = 3
# call our sum function and store the result in "result":
result = sum_two_values(first, second)
# print the result to the console:
print (result)

def sum_all(values):
    total = 0
    # loop through all values, and add them to total
    for value in values:
        total = total + value
    return total
        
values = [3,4,5]
# Call the sum_all function, pass it "values".
print(sum_all(values))
