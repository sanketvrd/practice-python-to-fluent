#program that takes input from an user  and gives all the divisors

number= int(input("Enter the number to get all the divisors :"))

list = list(range(2,number+1))


for x in list:
    if number%x ==0:
        print("The divisors are:" + str(x))