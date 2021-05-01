from threading import *
from time import sleep


class Hello(Thread):
    def run(self):  # run is an inbuilt method of thread
        for i in range(5):
            print("Hello")
            sleep(1)  # if we don't specify Hello and Hi will be printed on the same line and so we are making this
            # thread to sleep for 1 seconds


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()  # t1 thread prints Hello
t2 = Hi()  # t2 thread prints Hi
t1.start()  # t1 thread does the execution and becomes inactive for a while and meanwhile the t2 thread execution will
# be done
sleep(0.5)
# since run is an inbuilt method , start is used to initiate the thread and gets initialized to run method to do the
# execution
t2.start()

t1.join()  # in order to avoid collision we are using join in which the t1 thread and t2 thread execution are done
# systematically and finally the main thread execution will be done
t2.join()
print("Bye")  # this execution is done by the main thread
