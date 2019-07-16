def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

obj=fib(10)
print(obj)
print(next(obj))
for elem in obj:
    print(elem,end=" ")
