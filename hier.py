class A:
    def m1(self):
        return "1"
    def m2(self):
        return"2"
class B(A):
    def m3(self):
        return "3"
    def m4(self):
        return"4"
class C(A):
    def m5(self):
        return "5"
    def m6(self):
        return"6"
class D(A):
    def m7(self):
        return "7"
    def m8(self):
        return"8"
a=A()
print(a.m2())
b=B()
print(b.m1())
c=C()
print(c.m1())
d=D()
print(d.m1())
