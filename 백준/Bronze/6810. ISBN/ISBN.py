isbn_fixed = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]


digit1 = int(input())
digit2 = int(input())
digit3 = int(input())

isbn_fixed.append(digit1)
isbn_fixed.append(digit2)
isbn_fixed.append(digit3)


one_three_sum = 0
for i in range(13):
    if i % 2 == 0:
        one_three_sum += isbn_fixed[i] * 1  
    else:
        one_three_sum += isbn_fixed[i] * 3  
print(f"The 1-3-sum is {one_three_sum}")
