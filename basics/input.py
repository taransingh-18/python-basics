a = input("Enter number 1: ")
b = input("Enter number 2: ")

print("Number a is:", a)
print("Number b is:", b)    

print("Sum of a and b is(as str):", a + b)  # This will concatenate the strings instead of adding the numbers
print("Sum of a and b is:", int(a) + int(b))  # This will now add the numbers correctly

# input() returns string, so we convert to int for addition

c = int(input("Enter Number 3:"))
d = int(input("Enter Number 4:"))

print("Sum of c and d is:", c + d)  # This will add the numbers correctly since they are already converted to int