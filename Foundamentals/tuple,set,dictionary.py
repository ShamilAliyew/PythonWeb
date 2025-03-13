l=[]
firsList=['*']
s=1
say=97
s1=int(input())
s2=int(input())
for i in range(s1-1):
    firsList.append(str(s))
    s+=1
for x in range (s2):
    b = []
    b.append(chr(say))
    say+=1
    for i  in range(s1-1):
        b.append("*")
    l.append(b)
print(firsList)
for x in range (len(l)):
    print(l[x])
