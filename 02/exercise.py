def compute_pay(hours, rate):
    pay = 0
    rest_hours = hours
    if hours > 40:
        overtime = hours - 40
        over_pay = overtime * 1.5 * rate
        pay += over_pay
        rest_hours = 40

    pay += rest_hours * rate
    return pay


print(compute_pay(45, 10))
