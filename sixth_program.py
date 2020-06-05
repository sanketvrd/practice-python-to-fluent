#palindrom of a number


a = input("Enter  the string: ")

b =a[0:]
print(b)

c = a[::-1]
print(c)

if b==c:
    print("Palindrome")
else:
    print("not palindrome")