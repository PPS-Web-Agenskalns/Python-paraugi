ievade = "23313+123-2+12"

#2.uzd
cip = 0
summa = 0
irNegativs = False

for c in ievade:
    if ord(c)>=48 and ord(c)<=57:
       cip = cip * 10
       cip = cip + (ord(c)-48)

    else:
        
            
        if irNegativs == True:
            irNegativs = False
            cip = cip * -1

        if c == '-':
            irNegativs = True
        
        

        print(cip)
        summa = summa + cip
        print("summa: ", summa)
        cip = 0

print(cip)
summa = summa + cip
print("summa: ", summa)






