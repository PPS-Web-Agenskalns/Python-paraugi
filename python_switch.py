
def add():
    print("saskaitit")
def sub():
    print("atnemtfunc")
def div():
    print("dalit")
    
operacija = {
    '1': add,
    '2': div,
    "atnemt":sub,
}

operacija[input()]()

