text = "3 4 5 6"
result = 0
number = ""
for i in range(len(text)):
    if text[i] !=" ":
        result = int(text[i])*2
        number += str(result)+ (" ")
print(number)