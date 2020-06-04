# compare teo list and print the results that match in new list
import random
a = list(range(12, random.randint(32,39)))

b = list(range(2, random.randint(16,21)))

y=[]

for x in a:
    if x in b:
        y.append(x)

print(y)