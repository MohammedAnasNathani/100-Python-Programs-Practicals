def split_bill():
    total_amount = float(input("Enter the total bill amount: $"))
    num_people = int(input("Enter the number of people: "))
    
    tip = total_amount * 0.12
    total_with_tip = total_amount + tip
    amount_per_person = total_with_tip / num_people

    print(f"Tip: ${tip:.2f}")
    print(f"Total amount with tip: ${total_with_tip:.2f}")
    print(f"Amount per person: ${amount_per_person:.2f}")

split_bill()
