class A:
    def m1(self):
        return "hi"
    def m2(self):
        return"hello"
class B:
    def m3(self):
        return "hii"
    def m4(self):
        return"hello0"
class C(A,B):
    def m5(self):
        return "hii"
    def m6(self):
        return"hello0"



c=C()
print(c.m5())
print(c.m6())
print(c.m3())
print(c.m1())
