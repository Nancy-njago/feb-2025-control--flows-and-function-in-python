def calculate_discount(price, discount_percent):

    #Calculate the final price after applying a discount if it's 20% or higher.
    # i no discount is applied return the original price
    if discount_percent >= 20: 
     return price * (1 - discount_percent / 100)
    else:
     return price

# Have  users input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print result
    if final_price == price:
        print(f"No discount applied. The original price is: ${price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError as e:
    print(f"Invalid input! Please enter numeric values. Error: {e}")
