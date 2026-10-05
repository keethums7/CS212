# Lab 1 - Group A - Part 2 (beta) - Keith Wangler


# display directions for the user
print("\n--- Financial Product Recommendation System ---")

# dictionary for quick lookup based on user input
recommend_prod = {
    "short-term": {
        "low": "High-Yield Savings Account",
        "high": "Short-Term Corporate Bonds",
    },
    "long-term": {
        "low": "Government Bonds/Index Fund",
        "high": "Diversified Stock Portfolio",
    }
}

print("\nThis program is designed to recommend an investment product" \
      "\nbased on your investment horizon (short-term or long-term)" \
      "\nand your risk tolerance (low or high).")

is_valid = False

# loop until valid input is received
while not is_valid:
    # get user input for investment horizon, handle case sensitivity
    inv_horizon = input("\nEnter your investment horizon (Short-Term or " \
                    "Long-Term): ").lower()

    # get user input for risk tolerance, handle case sensitivity
    risk = input("Enter your risk tolerance (Low or High): ").lower()

    # check if the inputs are valid and set valid to True, otherwise loop
    if inv_horizon in recommend_prod and risk in recommend_prod[inv_horizon]:
        is_valid = True 
        print(f'\nBased on your investment horizon of "{inv_horizon}"' \
            f'\nand your risk tolerance of "{risk}", ' \
            f'\nwe recommend the following investment product:' \
            f'\n {recommend_prod[inv_horizon][risk]}')

    # display error message to guide user towards valid input
    else:
        print("\n--- ERROR: Invalid input received. ---" \
              "\nPlease enter valid options for investment horizon and risk tolerance.")