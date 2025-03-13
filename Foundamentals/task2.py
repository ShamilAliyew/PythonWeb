sentence='Thisisnotourfirstlesson' 
a=[]
for i in range(0,len(sentence),2):
    a.append(sentence[i:i+2])
    new=" ".join(a)
print(new)