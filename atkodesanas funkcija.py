ievade = "2*5"

izvade = 0
summa = 0
irMinuss = False
irReiz = False
irDal = False

List = []

for c in ievade:
    asci = ord(c)
    
    if asci<=57 and asci>=48:
        skaitlis = asci - 48;
        izvade = izvade * 10 + skaitlis;
        
        
    else:
        

        if irMinuss == True:
            izvade = izvade * -1 
            irMinuss = False

        if c == '-':
            irMinuss = True

        if irReiz == True:
            izvade = izvade * List.pop()
            irReiz = False

        if c == '*':
            irReiz = True

        if irDal == True:
            izvade = List.pop() / izvade
            irDal = False

        if c == '/':
            irDal = True
        
        List.append(izvade)
        izvade = 0
            

if irMinuss == True:
    izvade = izvade * -1 
    irMinuss = False

if c == '-':
    irMinuss = True

if irReiz == True:
    izvade = List.pop() * izvade
    irReiz = False

if c == '*':
    irReiz = True

if irDal == True:
    izvade = List.pop() / izvade
    irDal = False

if c == '/':
    irDal = True
        
List.append(izvade)
izvade = 0

print("summa", sum(List))
