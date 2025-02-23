print("Your age:")

age = int(input())

print('you are allowed to drive' if (age >= 18) else f'you are allowed to drive car after {18-age} years')