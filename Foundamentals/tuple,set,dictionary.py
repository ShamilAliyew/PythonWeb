# l=[]
# firsList=['*']
# s=1
# say=97
# s1=int(input())
# s2=int(input())
# for i in range(s1-1):
#     firsList.append(str(s))
#     s+=1
# for x in range (s2):
#     b = []
#     b.append(chr(say))
#     say+=1
#     for i  in range(s1-1):
#         b.append("*")
#     l.append(b)
# print(firsList)
# for x in range (len(l)):
#     print(l[x])


# Daha optimal
l=[]
start = ord('a')-1
for i in range(4):
    a=[]
    for j in range(4):
        if i==0:
            if j==0:
                j='*'
        else:
            if j==0:
                j=chr(start)
            else:
                j='x'
        a.append(format(str(j),' >2'))
    start +=1
    l.append(a)

for i in l:
    print("".join(i))