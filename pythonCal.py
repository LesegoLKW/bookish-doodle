# calculator.py

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n===== CALCULATOR RESULTS =====")

print(f"Addition:        {round(num1 + num2, 2)}")
print(f"Subtraction:     {round(num1 - num2, 2)}")
print(f"Multiplication:  {round(num1 * num2, 2)}")

if num2 == 0:
    print("Division:        Error - Cannot divide by zero")
    print("Floor Division:  Error - Cannot divide by zero")
    print("Modulus:         Error - Cannot divide by zero")
else:
    print(f"Division:        {round(num1 / num2, 2)}")
    print(f"Floor Division:  {round(num1 // num2, 2)}")
    print(f"Modulus:         {round(num1 % num2, 2)}")