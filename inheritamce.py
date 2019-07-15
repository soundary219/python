class A:
    def m1(self):
        return "hi"
    def m2(self):
        return"hello"
class B(A):
    def m3(self):
        return "hii"
    def m4(self):
        return"hello0"
class C(B):
    def m5(self):
        return "hii"
    def m6(self):
        return"hello0"


a=A()
print(a.m1())
print(a.m1())
print()
b=B()
print(b.m3())
print(b.m4())
print(b.m1())
print(b.m2())
print()
c=C()
print(c.m5())
print(c.m6())
print(c.m3())
print(c.m1())


