# mortgage.py
#
# Exercise 1.7, 1.8, 1.9, 1.10, 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    extra_payment_for_month = extra_payment if extra_payment_start_month <= month <= extra_payment_end_month else 0
    monthly_payment = payment + extra_payment_for_month
    principal = principal * (1+rate/12) - monthly_payment if monthly_payment < principal else 0
    total_paid = total_paid + monthly_payment
    print(month, total_paid, principal)

print(f'Total paid {total_paid}')
print(f'Months {month}')
