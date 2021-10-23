# Problem Set 2

## Question 1
def minimum_one_year(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        monthlyPayment = balance * monthlyPaymentRate
        balance -= monthlyPayment
        balance += annualInterestRate/12.0 * balance
    return round(balance, 2)


## Question 2
def low_payment(balance, annualInterestRate):
    for payment in range(10, balance, 10):
        total = balance
        for i in range(12):
            total -= payment
            total += total * (annualInterestRate / 12.0)
        if total <= 0:
            return payment


## Question 3
def lowest_payment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    lower = balance / 12.0
    upper = balance * (1 + monthlyInterestRate) ** 12 / 12.0
    epsilon = 0.009
    while True:
        payment = (upper + lower) / 2
        total = balance
        for i in range(12):
            total -= payment
            total += total * monthlyInterestRate
        if epsilon >= total >= 0:
            return round(payment, 2)
        if total < 0:
            upper = payment
        else:
            lower = payment
