text = "9394884039"
isFound = False
for i in range(len(text)):
    if text[i] =="8" and not isFound == True:
        print(i)
        isFound = True