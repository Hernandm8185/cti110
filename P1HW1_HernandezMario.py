# Mario Hernandez
# 3/30/2005
# P1HW1

print('----Calculating Exponents----\n')
print()

base = int(input('Enter an integer as the base value: '))
exponent = int(input('Enter an integer as the exponent value: '))

print()

result = base ** exponent

print(base, 'raised to the power of', exponent, 'is', result, '!!')
print()

print('\n----Addition and Subtraction----\n')
print()

num1 = int(input('Enter a starting integer: '))
num2 = int(input('Enter an integer to add: '))
num3 = int(input('Enter an integer to subtract: '))

print()

result = (num1 + num2) - num3

print(num1, "+", num2, "-", num3, "is equal to", result)
