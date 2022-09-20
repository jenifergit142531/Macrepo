def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def weekends():
    return "Saturday and Sunday"
def default():
    return "Invalid day"

switcher ={
    1:monday,
    2:tuesday,
    3:wednesday,
    4:thursday,
    5:friday,
    6:weekends
}

def switch(dayofweek):
    return switcher.get(dayofweek,default)()


print(switch(3))
print(switch(10))