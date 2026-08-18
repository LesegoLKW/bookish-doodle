kilometers = float(input("How many kilometers will you drive? "))
petrol_price = float(input("Enter the petrol price per liter: R"))

liters_needed = kilometers / 10
total_cost = liters_needed * petrol_price

print(f"Kilometers: {kilometers} km")
print(f"Fuel Needed: {liters_needed:.2f} liters")
print(f"Total Cost: R{total_cost:.2f}")
