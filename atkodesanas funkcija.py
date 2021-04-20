ievade = "1212-21+3"

izvade = 0
summa = 0
irMinuss = False
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
            
        
            
        print(izvade)
        summa = summa + izvade
        izvade = 0
        print("Seit ir", c)

        

        



    
    """ #veca versija:
    if c == '+':
        print(izvade)
        izvade = ""
        print("Seit ir plusins")

    else:
        izvade = izvade + c
    """

print(izvade)
summa = summa + izvade

print("summa", summa)
