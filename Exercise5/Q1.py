text = "454639"
count_even = 0
count_odd = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(count_even, count_odd)