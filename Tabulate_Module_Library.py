from tabulate import tabulate

employees = [
    {
        "ID": 1, 
        "Name": "Sk. Salahuddin", 
        "Age": 35,
        "Country": "Finland", 
        "Phone": 35804571234567, 
        "Email": "quantam_c@ping.au.p"
    },
    {
        "ID": 2, 
        "Name": "Nisa Rehman", 
        "Age": 45,
        "Country": "Australia", 
        "Phone": 61450671001, 
        "Email": "mariana@gmail.com"    
    },
    {
        "ID": 3, 
        "Name": "Ilma Rehman", 
        "Age": 3,
        "Country": "Australia", 
        "Phone": 61450671002, 
        "Email": "level@gmail.com"
    },
    {
        "ID": 4, 
        "Name": "Zahid Rehman", 
        "Age": 50,
        "Country": "United Kingdom", 
        "Phone": 447740054977, 
        "Email": "some@gmail.com"
    }
]
print(tabulate(employees, headers="keys", tablefmt="rounded_grid"))

#--------------------------------------Another Code-----------------------------------------------

from tabulate import tabulate
employee = [
  {"ID": 1, "Name": "Sk. Salahuddin", "Age": 35, "Country": "Finland", "Phone": 8801767902828},
  {"ID": 2, "Name": "Ilma Rehman", "Age": 3, "Country": "Australia", "Phone": 6564332114},
  {"ID": 3, "Name": "Aminul Islam", "Age": 50, "Country": "United Kingdom", "Phone": 4474251783},
  {"ID": 4, "Name": "Nisa Zannat", "Age": 45, "Country": "Australia", "Phone": 6541674267}
]
result = tabulate(employee, headers="keys", tablefmt="fancy_grid")
print(result)
#print(tabulate(employee, headers="keys", tablefmt="pretty"))
