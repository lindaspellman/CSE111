from datetime import datetime

import math

discount = 0
difference = 0

current_date_and_time = datetime.now()

weekday = current_date_and_time.isoweekday()

sub_total = float(input("What is your subtotal? "))

if sub_total == 50 and (weekday == 2 or weekday == 3):
    discount = sub_total * 0.1
    sub_total = sub_total - discount
    print(f"Discount: ${discount:.2f}")

elif sub_total < 50 and (weekday == 2 or weekday == 3):
    difference = 50 - sub_total
    print(f"If you spend ${difference:.2f} more, you can get a 10% discount!")

tax = sub_total * 0.06
total = sub_total + tax
print(f"Sales tax amount: ${tax:.2f}")
print(f"Total: ${total:.2f}")