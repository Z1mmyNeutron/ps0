portion_downpayment = .25
r = 0.04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter percent of your salary to save as a decimal: "))
total_cost = float(input("How much is your dream home? "))
semi_annual_raise = float(input("Enter the semi-annual raise as a decimal: "))

current_savings = 0.0
monthly_salary = annual_salary / 12
monthly_return_rate = r / 12
down_payment = total_cost * portion_downpayment
months = 0

while current_savings < down_payment:
    current_savings += current_savings * monthly_return_rate
    current_savings += monthly_salary * portion_saved
    if months % 6 == 0 and months != 0:
        monthly_salary += monthly_salary * semi_annual_raise
    months += 1


print("Number of months: ", months)