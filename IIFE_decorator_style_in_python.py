@lambda _: _()
def func() -> bool:
    print('func()')
    return True

# Answer: func()

#-----------------------------------------------------------

@lambda _: _()
def func() -> bool:
    print('func()')
    return True
    
print(func)

# Answer: func()
#         True

#-----------------------------------------------------------

from datetime import datetime

@lambda _: _()
def func() -> str:
    time_text: str = f'Started at: {datetime.now():%H:%M:%S %p %a}'
    print(time_text)
    return time_text
    
# Answer: Started at: 12:14:56 PM Fri

#------------------------------------------------------------

from datetime import datetime

@lambda _: _()
def func() -> str:
    time_text: str = f'Started at: {datetime.now():%H:%M:%S %p %a}'
    print(time_text)
    return time_text
    
print(func)

# Answer: Started at: 12:14:56 PM Fri
#         Started at: 12:14:56 PM Fri

#------------------------------------------------------------

from datetime import datetime

@lambda _: _()
def func() -> str:
    time_text: str = f'Started at: {datetime.now():%H:%M:%S}'
    print(time_text)
    return time_text
    
# Answer: Started at: 12:14:56

#------------------------------------------------------------

from datetime import datetime

@lambda _: _()
def func() -> str:
    time_text: str = f'Started at: {datetime.now():%H:%M:%S}'
    print(time_text)
    return time_text
    
print(func)

# Answer: Started at: 12:14:56 
#         Started at: 12:14:56 
