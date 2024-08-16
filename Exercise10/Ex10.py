numbers = ""
for i in range(5):
    result = input("Enter number: ")
    numbers+=str(result)
    max_number = numbers
    min_number = numbers
    for i in range(len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
        elif numbers[i] < min_number:
            min_number = numbers[i]
print(max_number)
print(min_number)
