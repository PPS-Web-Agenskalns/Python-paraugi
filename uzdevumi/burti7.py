ievade = input()
izvade = ""

a = input()
b = input()

for x in ievade:
   if x == a:
      #izvade = izvade + b tas pats kas rindinu zemak
      izvade += b
   else:
      izvade += x
   

'''for x in range(0, len(ievade)):
  if ievade[x] == a:
     ievade[x] = b'''

print(ievade)
   
