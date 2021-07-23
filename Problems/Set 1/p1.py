
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
total_cost = float(input("The cost of your dream home: "))

r = 0.04
portion_down_payment = 0.25
current_savings = 0
months = 0

monthly_salary = annual_salary / 12
monthly_return = r / 12

down_payment = portion_down_payment * total_cost

while down_payment >= current_savings:

    current_savings += monthly_salary*portion_saved + monthly_return*current_savings
    months += 1

print("Months needed: ",months)
