ievade = "1212+21+3"

izvade = ""
for c in ievade:
    
    if c == '+':
        print(izvade)
        izvade = ""
        print("Seit ir plusins")

    else:
        izvade = izvade + c

print(izvade)
