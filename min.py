n=int(input("enter number"))
lst=[]
temp=0

 
for i in range(n):
    lst.append(int(input()))

temp=lst[0]

for i in range(1,n,1):
    if temp>lst[i]:
        temp=lst[i]
        
print(temp)

