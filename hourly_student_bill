week = []
cost = []
total_cost = 0
output_week = 0
output_day = []

for i in range(1,7+1):
    minute = int(input("Enter your working minutes: "))
    week.append(minute)
send_money = int(input("Send Money from Client: "))

for i in range(1,7+1):
    everyday_cost = int(input("Enter your daily costs: "))
    cost.append(everyday_cost)
    total_cost = total_cost + everyday_cost
    
for i in week:
    if i >= 4*60:
        while True:
            i = 4*60
            break
        day = i * (50/60)
        week = day
        output_week = output_week + week 
        output_day.append(day)
    if i < 4*60 and i > 0:
        day = i * (50/60)
        week = day
        output_week = output_week + week
        output_day.append(day)
print(output_week)
print(output_day)
print(cost)
smtc = send_money-total_cost
print(smtc)
print(smtc-output_week)
