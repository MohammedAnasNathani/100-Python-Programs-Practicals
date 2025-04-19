def calculate_earnings():
    hourly_wage = float(input("Enter hourly wage: $"))
    hours_worked = float(input("Enter hours worked: "))
    
    total_earnings = hourly_wage * hours_worked
    print(f"Total earnings: ${total_earnings}")

calculate_earnings()
