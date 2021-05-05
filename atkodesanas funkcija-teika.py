ievade = "23*4+231/23*4-2*3"

#2.uzd
cip = 0
summa = 0
List = []
irNegativs = False
irReiz = False
irDal = False


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

        if irReiz == True:
            irReiz = False
            cip = cip * List.pop()

        if c == '*':
            irReiz = True

        if irDal == True:
            irDal = False
            cip = cip / List.pop()

        if c == '/':
            irDal = True
        
        List.append(cip)
        cip = 0
        print(List)

#summa = summa + cip
#print("summa: ", summa)

if irNegativs == True:
    irNegativs = False
    cip = cip * -1


if irReiz == True:
    irReiz = False
    cip = cip * List.pop()

if irDal == True:
    irDal = False
    cip = cip / List.pop()
        
List.append(cip)
print("Sum:", sum(List))






