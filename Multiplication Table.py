# Multiplication Table

print("Welcome to the Multiplication Table Machine")
print("--"*20)

try:
    num1 = int(input("Enter a Number: "))
    for i in range(1, 11):
        print(f"{num1} x {i} = {num1*i}")

except:
    print("You entered a non-integer/string")
    print("Please Run the program again and try entering a number")
    exit()

a = input("Press Enter to quit")
# Programme Runned Succesfully