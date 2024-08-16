text ="3 4 5 6"
sum = 0
for i in range(len(text)):
    if text[i] != " ":
        sum +=int(text[i])
print(sum)