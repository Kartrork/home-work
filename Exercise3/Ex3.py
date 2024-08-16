text = input("Please enter text: ")
result = ""
for i in range(len(text)):
    if text[i] .isupper():
        result=("Yes")
    else:
        result=("No")
print(result)