text = "454639"
even_number = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        even_number += int(text[i])
print(even_number)