# Lab 1 - Group A - Part 1 (beta) - Keith Wangler


# define a function to handle cost calculation logic
def calculate_shipping_cost(is_valid, weight_kg, zone):
    z = zone.capitalize()

    if z == "A":
        if weight_kg <= 5:
            cost = 10.00
        elif weight_kg <= 10:
            cost = 15.00
        else:
            cost = 20.00
    elif z == "B":
        if weight_kg <= 5:
            cost = 15.00
        elif weight_kg <= 10:
            cost = 20.00
        else:
            cost = 25.00
    elif z == "C":
        if weight_kg <= 5:
            cost = 20.00
        elif weight_kg <= 10:
            cost = 25.00
        else:
            cost = 30.00
    else:
        print("Error: Invalid shipping zone entered.")
        is_valid = False

    # output results if is_valid returns True
    if is_valid:
        print(f"Package Details: {weight_kg}kg to Zone {z}")
        print(f"Calculated Shipping Cost: ${cost:.2f}")

    print("----------------------------")


# first example run
# declare variables
weight_kg = 7.5
zone = "A"
cost = 0.0
is_valid = True

print("\n--- Shipping Cost Check (Procedural) ---")
calculate_shipping_cost(is_valid, weight_kg, zone)

# second example run
# declare variables
weight_kg = 12.0
zone = "C"
cost = 0.0
is_valid = True

print("\n--- Shipping Cost Check (Second Run) ---")
calculate_shipping_cost(is_valid, weight_kg, zone)