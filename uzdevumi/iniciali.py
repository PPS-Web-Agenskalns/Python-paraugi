ievade = input()
irAtstarpe = False
otrsBurts = ''

for x in range(0, len(ievade)):
   if ievade[x] == ' ':
      otrsBurts = ievade[x+1]

print(ievade[0] + '.' + otrsBurts + '.')
