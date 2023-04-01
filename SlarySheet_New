month=int(input("enter no of days :"))
holidays=int(input("enter no of holidays :"))
working_days=int(month-holidays)
print(working_days)

salary_per_day=int(input("enter the daily salary :"))
monthly_salary=int(month*salary_per_day)
print(monthly_salary)

late_entry=int(input("enter the no of late days :"))
early_leave=int(input("enter the no of early left days :"))
total_salary=monthly_salary

late_count=0

active=False
for i in range(late_entry):
    late_count+=1
    if late_count ==3:
        total_salary=total_salary-salary_per_day
        late_count=0
        active=True
    if bool(active):
        a=salary_per_day/3
        total_salary-=a

early_leave_counter=0
for i in range(early_leave):
    early_leave_counter+=1
    if early_leave_counter ==4:
        total_salary=total_salary-salary_per_day
        early_leave_counter=0

print(total_salary)
