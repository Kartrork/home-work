number = input("Enter number:")
result = 0
for i in range(len(number)):
    if int(number[i]) % 2 == 0:
        result =("Even number")
    else:
        result =("Odd number")
print(result)