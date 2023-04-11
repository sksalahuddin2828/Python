class SalarySheet:
    def __init__(self,working_day,salary_per_day,late_entry,early_leave):
        self.working_day=working_day
        self.salary_per_day=salary_per_day
        self.late_entry=late_entry
        self.early_leave=early_leave
    def prosses(self):
        return self
akash=SalarySheet(30,100,3,4)
tanin=SalarySheet(30,100,6,5)
rafi=SalarySheet(30,100,30,8)

monthly_salary=30*akash.prosses().salary_per_day
print(monthly_salary)
late_entry=akash.prosses().late_entry
early_leave=akash.prosses().early_leave
total_salary=monthly_salary
late_count=0

total_salary=monthly_salary
late_count=0
for i in range(late_entry):
    late_count+=1
    if late_count ==3:
        total_salary=total_salary-akash.prosses().salary_per_day
        late_count=0

early_leave_counter=0
for i in range(early_leave):
    early_leave_counter+=1
    if early_leave_counter ==4:
        total_salary=total_salary-akash.prosses().salary_per_day
        early_leave_counter=0
print(total_salary)
