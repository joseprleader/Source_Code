# Module 4 of PY4E: Conditional Statements Exercise 3.1

# Input 45 hours and 10.50 as rate per hour

hours = float(input("Enter Hours:"))
rate = float(input("Enter Hourly Rate: "))

if hours > 40:
    normal_pay = 40 * rate
    extra_hours = hours - 40
    extra_rate = rate * 1.5
    extra_pay = extra_hours * extra_rate
    pay = normal_pay + extra_pay
    
else:
    pay = hours * rate

print(pay)
