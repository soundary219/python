import threading
import time

def cubes():
    for i in range(1,10):
        print("cubes={}".format(i**3),end=" ")
        time.sleep(5)

def squares():
    for i in range(1,10):
        print("squares={}".format(i**2),end=" ")

if __name__=='__main__':    
    #creating a thread
    t1=threading.Thread(target=cubes,args=())
    t2=threading.Thread(target=squares,args=())
    #start thread
    t1.start()
    t2.start()

    print('Thread count:{}'.format(threading.active_count()))
    print(t1.is_alive())
    print(t2.is_alive())
    #get thread
    t1.setName("t1")
    t2.setName("t2")
    print(t1.getName())
    print(t2.getName())



    t1.join()
    t2.join()
    for i in range(1,10):
        print(i,end=" ")
        time.sleep(5)
        