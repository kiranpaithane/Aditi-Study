from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):                     
        for i in range(5):
            print("HI")
            sleep(1)


h1 = Hello()
h2 = Hi()

h1.start()    # main thread 
h2.start()    # main thread    













# Main Thread 














'''

from threading import *


class Hello(Thread):
    def run(self):
        for i in range(100):
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(100):
            print("HI")


h1 = Hello()
h2 = Hi()

h1.start()
h2.start()
'''
# it creates 2 threads
























#join()


'''
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("HI")


h1 = Hello()
h2 = Hi()

h1.run()
h2.run()


'''