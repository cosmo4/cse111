from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

subtotal = float(input('What is the subtotal: $'))

if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
    new_subtotal = subtotal *.9
    tax_amount = new_subtotal * .06
    discount = subtotal - new_subtotal
    total = new_subtotal * 1.06
    print(f'Discount amount: ${discount:.2f}')
    print(f'Sales tax amount: ${tax_amount:.2f}')
    print(f'Total: ${total:.2f}')
else:
    tax_amount = subtotal * .06
    discount = 0
    total = subtotal * 1.06
    print(f'Sales tax amount: ${tax_amount:.2f}')
    print(f'Total: ${total:.2f}')

    


