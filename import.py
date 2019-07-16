from threading import Thread
import time

class A(Thread):
    def run(self):
        for i in range(1,3):
            print(i**3)
            time.sleep(1)
class B(Thread):
    def run(self):
        for i in range(1,3):
            print(i**2)
            time.sleep(1)

a=A()
b=B()

a.start()
b.start()

a.join()
b.join()

for i in range(1,3):
    print("hi")
    time.sleep(1)