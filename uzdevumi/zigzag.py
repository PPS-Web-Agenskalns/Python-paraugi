ievade = input()


izvade = ""

for x in range(0, len(ievade), 4):
   izvade += ievade[x]

for x in range(1, len(ievade), 2):
   izvade += ievade[x]

for x in range(2, len(ievade), 4):
   izvade += ievade[x]

print(izvade)



