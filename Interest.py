"""Write a function howManyyears(start, rate, savings, target) where:

start - the starting balance in your retirement account (float)

rate - the yearly interest rate (float) - like 0.001 for 0.1%

saving - the yearly amount saved for retirement (float)

target - the target retirement that you’d like to achieve

The function returns how many years it takes to reach target retirement amount. 

So, next_month_balance = start_balance * (1 + rate) + savings"""

def howManyyears(start, rate, savings, target):
    balance = start
    years = 0
    
    while (balance >= 0 and balance < target and years < 30):
        balance = balance * (1 + rate) + savings
        years += 1
    
    if balance >= target  :
        return years
    else:
        return -1
    
x=howManyyears(1000, .10, 1000, 1000000)
print(x)

states = ["Washington","Montana","Michigan","New York","Idaho","Minnesota","Massachusetts"]
i = 0
length = len(states)
m_counter = 0
while i < length:
    word=(states[i])
    if word[0] == "M":
        print(word)
        m_counter = m_counter + 1
    i += 1

def howManyMonths(start, rate, spending, target):
    balance = start
    months = 0
    
    while (balance >= 0 and balance < target and months < 100):
        balance = balance * (1 + rate) - spending
        months += 1
    if balance >= target:
        return months
    else:
        return -1
x = howManyMonths(480.00, .09, 150.00, 502)  
print(x)
