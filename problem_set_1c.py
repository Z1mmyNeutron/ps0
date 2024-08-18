portion_downpayment = 0.25
total_cost = 1000000
semi_annual_raise = 0.07
annual_return_rate = 0.04
monthly_return_rate = annual_return_rate / 12
down_payment = total_cost * portion_downpayment

def calculate_months_to_save(portion_saved, annual_salary):
    current_savings = 0.0
    monthly_salary = annual_salary / 12
    months = 0
    
    while current_savings < down_payment:
        current_savings += current_savings * monthly_return_rate
        current_savings += monthly_salary * portion_saved
        months += 1
        
        if months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    
    return months

def best_saved_portion(annual_salary):
    low = 0
    high = 1
    epsilon = 0.01
    number_of_guesses = 0
    
    while low <= high:
        best_saved = (high + low) / 2
        months_needed = calculate_months_to_save(best_saved, annual_salary)
        
        if months_needed <= 36:
            high = best_saved - epsilon
        else:
            low = best_saved + epsilon
        
        number_of_guesses += 1
        if number_of_guesses > 100:  # Safeguard to prevent infinite loop
            return None
    
    # Ensure the best_saved is within the bounds
    if low > high:
        best_saved = (high + low) / 2
    else:
        best_saved = None
    
    return best_saved

def main():
    annual_salary = float(input("Enter the starting salary: "))
    
    portion_saved = best_saved_portion(annual_salary)
    
    if portion_saved is not None:
        months = calculate_months_to_save(portion_saved, annual_salary)
        if months <= 36:
            print(f"The best savings rate is: {portion_saved:.4f}")
            print(f"Number of months to reach the down payment: {months}")
        else:
            print("It's not possible to save enough in 36 months with the given parameters.")
    else:
        print("It's not possible to save enough in 36 months with the given parameters.")

main()
