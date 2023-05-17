# Tip Calculator

print("Welcome to the tip calculator!")

bill = float(input("Please enter total bill amount: \n$"))

head_count = int(input("How many people in your party?\n"))

tip = float(input("What percentage tip would you like to give? Type a whole number. (15 is customary, decrease "
                  "or increase according to value of service received.)\n"))

tip_total = (tip / 100) * bill
total_bill = bill + tip_total
tip_total_print = "{:.2f}".format(tip_total)

pay_each = "{:.2f}".format(total_bill/head_count)
message = f"You each need to pay ${pay_each}. (The total tip is ${tip_total_print})."

print(message)

