annual_salary = float(input("The starting annual salary:"))

cpy_annual_salary = annual_salary

current_savings = 0
total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25

monthly_salary = annual_salary / 12
monthly_return = r / 12

epsilon = 100
total_months = 36
months = 0
num_of_guesses = 0

down_payment = total_cost * portion_down_payment

low = 0
high = 100
#d.e.i.
guess_value = (low + high ) / 2
monthly_salary_guessed = monthly_salary * guess_value 

if ((3*annual_salary )+(annual_salary*r)) <= down_payment:
    print("not possible")
else:
    while abs(current_savings - down_payment) > 10000:
        current_savings = 0
        while months < 36:
                if (months % 6 == 0):
                    annual_salary = annual_salary + (semi_annual_raise * annual_salary)
                    monthly_salary_guessed = monthly_salary * guess_value 
                current_savings = current_savings + (current_savings * monthly_return) + monthly_salary_guessed
                months += 1
        num_of_guesses +=1
        annual_salary = cpy_annual_salary
        months = 0
        if abs(current_savings - down_payment) > 10000:
            if current_savings > down_payment:
                high = guess_value
            else:
                low = guess_value
            guess_value = (high + low) /2
            monthly_salary_guessed = monthly_salary * guess_value
        else:
            print("rate:", guess_value)
            print("bisection search:", num_of_guesses)
            break
