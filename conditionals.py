# conditional statements

# If-else statements

a = int(input("Enter one value : "))
if a % 2 == 0:
    print("\n", a, " is even ")

else:
    print("\n", a, " is odd ")

# if-elif-else

if a < 50:
    print("\n", a, "Student is failed ")

elif 50 <= a <= 80:
    print("\n", a, "Student is passed to next class with avg score ")
else:
    print("\n", a, "Student is passed with distinction  ")


