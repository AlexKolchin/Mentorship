print("Lets check if the numbers of apartment exist")
x = int(input("Enter the number of first apartment: "))
y = int(input("Enter the number of last apartment: "))
if y % (y-(x-1)) == 0:
    print("Yes")
else:
    print("No")