import pandas as pd

# read income data 
income_df = pd.read_csv("income.csv")

# read expense data
expenses_df = pd.read_csv("bills.csv")

# Read wishlist data (assuming the wishlist is in a file called wishlist.csv)
wishlist = pd.read_csv("wishlist.csv").to_dict(orient='records')  # Convert to list of dictionaries

def calculate_budget(income_df, expenses_df, wishlist):
    # Starting values
    checking_balance = 3000  # Starting balance in checking account
    savings_balance = 0  # Starting balance in savings account
    savings_over_time = []  # To track savings over time
    purchased_items = []  # To track purchased wishlist items
    
    # Assuming income_df contains information about bi-weekly income
    # Assuming expenses_df contains information about regular expenses
    
    for index, row in income_df.iterrows():
        income = row['Cost']  # Assuming the 'Cost' column has income data
        frequency = row['Frequency']
        
        # Check if the frequency is bi-weekly (i.e., every 2 weeks)
        if frequency == 2:  
            # Add income to checking account
            checking_balance += income
            
            # Process expenses for the pay period
            for _, expense in expenses_df.iterrows():
                # Check if the expense frequency is monthly or weekly or yearly
                if expense['Frequency'] == 1:  # Monthly expense
                    # Deduct monthly expenses from checking
                    checking_balance -= expense['Cost']
                elif expense['Frequency'] == 7:  # Weekly expense (you could adjust based on your needs)
                    checking_balance -= expense['Cost']
                # Add more logic here to handle yearly and other time measures as necessary

            # Deduct 10% of the remaining balance for savings
            savings_contribution = 0.1 * checking_balance
            savings_balance += savings_contribution
            checking_balance -= savings_contribution  # Move savings to savings account
            
            # Purchase wishlist items based on the savings amount
            for item in wishlist:
                if savings_balance >= item['Amount'] * 0.2:  # If 20% of savings is enough to buy the item
                    purchased_items.append(item['Item'])  # Add item to purchased items
                    savings_balance -= item['Amount']  # Deduct the cost from savings
            
            # Track savings over time
            savings_over_time.append(savings_balance)
        
    # Return final balances and other results
    return checking_balance, savings_balance, savings_over_time, purchased_items
# Call the function with the DataFrames and wishlist
final_checking, final_savings, savings_over_time, purchased_items = calculate_budget(income_df, expenses_df, wishlist)

# Print the results
print(f"Final Checking Account Balance: ${final_checking:.2f}")
print(f"Final Savings Account Balance: ${final_savings:.2f}")
print(f"Wishlist Items Purchased: {[item for item in purchased_items]}")

# Optionally, print savings over time
print("Savings Over Time:", savings_over_time)