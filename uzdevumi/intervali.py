n = int(input())
m = int(input())
arr = []
for x in range(n):
   arr.append(int(input()))

for i in range(m):
   x = int(input())
   y = int(input())
   summa = 0
   
   for i in range(x-1,y):
      summa += arr[i]

   print(summa)
      
