# Display name and student ID
name = input("Enter your name: ")
student_id = input("Enter your Student ID: ")

print("Student:", name)
print("Student ID:", student_id)

# Ask for two whole numbers
number1 = int(input("Enter the first whole number: "))
number2 = int(input("Enter the second whole number: "))

# Perform three calculations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2

# Display results with two decimal places
print(f"Addition result: {addition:.2f}")
print(f"Subtraction result: {subtraction:.2f}")
print(f"Multiplication result: {multiplication:.2f}")

# Determine which number is larger
if number1 > number2:
    print("The first number is larger than the second number.")
elif number1 < number2:
    print("The first number is smaller than the second number.")
else:
    print("Both numbers are equal.")
