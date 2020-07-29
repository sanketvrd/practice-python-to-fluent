a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

numbers=[]
uniques_list=[]

for each_in_a in a:
    for each_in_b in b:
        if each_in_a == each_in_b:

            numbers.append(each_in_a)


for unique in numbers:
    if unique not in uniques_list:
        uniques_list.append(unique)


print("Unique Elements:"+uniques_list)
print(numbers)