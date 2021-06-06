i = input().split(" ")

univ = []
d= {}
n = 0
printable = []
elem = []

while(n < int(i[0])):
       st = input()
       univ.append(st)
while(n < int(i[0])):
       st = input()
       if(st not in univ):
               univ.append(st)
               d[st] = 0
       if(d.get(st) < int(i[2])):
              printable.append(st)
              elem.append(n)
              d[st] += 1 
       n+=1

i1 = input().split(" ")
n = 0 
print(i[1])
while(n <= int(i[1])-1):
       cur  = univ[n]
       if(cur not in d.keys()):
               d[cur] = 0
       if(d.get(cur) < int(i[2])):
              print(d[cur] + " #" + i1[n])
              d[cur] += 1 
       n+=1