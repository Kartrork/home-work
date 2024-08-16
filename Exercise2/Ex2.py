text = input("Please enter text: ")
result =""
for i in range(len(text)):
    if text[i] =="a" or text[i] =="A":
        if len(text)-1:
             result = result + str(i)+"-"
        else:
            result = result + str(i)
print(result)