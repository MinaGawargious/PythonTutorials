# Script for paying off credit card, monthly
import datetime, calendar

balance = 5000
interest = 0.13
monthly = 500

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_of_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_of_month + 1) # Start payments on 1st of next month
print(start_date)

end_date = start_date

while balance > 0:
    interest_charge = (interest/12) * balance
    balance += interest_charge
    balance -= monthly
    
    balance = 0 if balance < 0 else round(balance)
    print(end_date, balance)
    
    # Move to next month:    
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month) # Move to next month's 1st