lst=[30,40,10,20,60,5]
for i in range(6):
    for j in range(i):
        if(lst[i]<lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)
