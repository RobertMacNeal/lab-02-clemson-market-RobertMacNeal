
print("Welcome to the Clemson Market!")
print("We have the following items available:\n")
print("Bag of Chips: $5.99 each")
print("Turkey Sandwich: $13.23 each")
print("Bananas: $2.73 per lb")

print("How many bags of chips do you want?")
amount_chips = int(input())
print("How many turkey sandwiches do you want?")
amount_tsw = int(input())
print("How many lbs of bananas do you want?")
lbs_banana = float(input())

price_chip = amount_chips * 5.99
price_tsw = amount_tsw * 13.23
price_banana = lbs_banana * 2.73

total_price = price_banana + price_chip + price_tsw
# TODO: Format below output correctly
print(f"Your total before tax is ${total_price:.2f}.")

print("Please enter the tax rate:")
tax_rate = float(input())
total_tax = total_price + total_price * (tax_rate/100)
# TODO: Format below output correctly
print(f"Your total after tax is ${total_tax:.2f}. Thank you for shopping at the Clemson Market!")