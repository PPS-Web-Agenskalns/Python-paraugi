ievade = "1212-21+3"

izvade = ""
for c in ievade:
    asci = ord(c)

    if asci<=57 and asci>=48:
        izvade = izvade + c
    else:
        print(izvade)
        izvade = ""
        print("Seit ir simbols")



    
    """ #veca versija:
    if c == '+':
        print(izvade)
        izvade = ""
        print("Seit ir plusins")

    else:
        izvade = izvade + c
    """

print(izvade)
