# program to get user name and age

name=input("What is your name?: ")
print("Your name:"+ name)

age = int(input("Please enter your age: "))

print("Your name:"+"\t"+str(age))

if age<100:
    year_born = 2020 - age
    year_turn_100 = year_born+100
    print("The year your turn 100:\t"+str(year_turn_100))
