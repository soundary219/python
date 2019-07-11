lst=[]
i=int(input())
rep={}
for r in range(i):
    lst.append(input())
for i in lst:
    if i in rep:
        rep[i]+=1
    else:
        rep[i]=1
print(len(rep))
k=[]
for i in rep.values():
    k.append(i)
print(k)
