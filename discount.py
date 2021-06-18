from datetime import datetime

current = datetime.now()
weekday = 3
# current.isoweekday()
subtotal = float(input("Please enter the subtotal: "))

if (subtotal >= 50.00) and ((weekday == 2) or (weekday == 3)):
    discount = subtotal * .1
    print(f"Discount amount: ${discount:.2f}")
    subtotal -= discount
elif (subtotal < 50.00) and ((weekday == 2) or (weekday == 3)):
    difference = 50 - subtotal
    print(f"If you pay an extra ${difference:.2f} or more, you can get a 10% discount on your whole purchase!")

tax = subtotal * .06

print(f"Sales tax amount: ${tax:.2f}")
print(f"Total: ${subtotal + tax:.2f}")