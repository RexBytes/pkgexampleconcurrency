import threading
import time
import random


class OutputAlpha(threading.Thread):
    def __init__(self, daemon: bool, sleeptime: int):
        threading.Thread.__init__(self)
        self.sleeptime = sleeptime
        self.daemon = daemon

    def run(self):
        for char in "abcdefg":
            time.sleep(self.sleeptime)
            print(char)


class MyThreading:
    def __init__(self):
        pass

    def print_evens(self):
        max_num = 6
        for i in range(0, max_num + 1, 2):
            time.sleep(max_num + 1 - i)
            print(i)

    def print_odds(self):
        max_num = 6
        for i in range(1, max_num + 1, 2):
            time.sleep(i + 1)
            print(i)

    def print_alpha(self):
        print(
            """#We define a class that inherits the Thread base class,

class OutputAlpha(threading.Thread):

     #Notice we have to overide the base constructor if we want to
     #pass in our own variables.
    def __init__(self, daemon: bool, sleeptime: int):
        threading.Thread.__init__(self)
        self.sleeptime = sleeptime
        self.daemon = daemon

     #We overide the run() method to carry out a task of our choice.
    def run(self):
        for char in "abcdefg":
            time.sleep(self.sleeptime)
            print(char)


     #and then call it from within another class method,
class MyThreading:
    def __init__(self):
        pass

    def print_alpha(self)
        output_alpha = OutputAlpha(daemon=True, sleeptime=1)
        output_alpha.start()
        output_alpha.join()

             """
        )
        output_alpha = OutputAlpha(daemon=True, sleeptime=1)
        output_alpha.start()
        output_alpha.join()

        print(
            """

We ran our thread class as a daemon thread class with joins,
so the main thread waited for the worker thread to finish. """
        )

    def non_daemon_concurrent_example(self):
        t1 = threading.Thread(target=self.print_evens)
        t2 = threading.Thread(target=self.print_odds)

        print(
            """
#This is a non daemon CONCURRENT thread example.
#You will see that odd and even numbers will print
#in mixed order as the threads run concurrently.
#This configuration of the use of .start(), and .join()
#will run your threads concurrently.

----
t1 = threading.Thread(target=self.print_evens)
t2 = threading.Thread(target=self.print_odds)

t1.start()
t2.start()

t1.join()
t2.join()
----

"""
        )

        # This configuration of .start() and .join() will run threads concurrently
        t1.start()
        t2.start()

        t1.join()
        t2.join()
        print(
            """This print statement is called at the end of the main thread, notice 
that when calling .join() on a worker thread this blocks the main thread until
the worker thread has finished its task.  This print statement is the last executed
code in the main thread"""
        )

    def non_daemon_no_join_concurrent_example(self):
        t1 = threading.Thread(target=self.print_evens)
        t2 = threading.Thread(target=self.print_odds)

        print(
            """
#This is a non daemon CONCURRENT thread example
#that does not call .join() on its worker threads.
#You will see that odd and even numbers will print
#in mixed order as the threads run concurrently.
#You will also see that non daemon threads, even when
#not having called join() will hold the main thread open
#untill their tasks complete.

----
t1 = threading.Thread(target=self.print_evens)
t2 = threading.Thread(target=self.print_odds)

t1.start()
t2.start()


----

"""
        )

        # This configuration of .start() and .join() will run threads concurrently
        t1.start()
        t2.start()

        print(
            """This print statement is called at the end of the main thread, notice 
that when NOT calling .join() on a worker thread this does not block the main thread
which is why you are seeing this print statement. However, a running non-daemon worker thread will
keep the main thread open until it finishes its work... which is why you are about to see
the worker threads continue to output numbers.  This main thread will exit when the worker thread is done.

"""
        )

    def non_daemon_serial_example(self):
        t1 = threading.Thread(target=self.print_evens)
        t2 = threading.Thread(target=self.print_odds)

        print(
            """
#This is a non daemon SERIAL thread example.
#You will see that odd and even numbers will print
#at diffent steps as the threads run SERIALY.
#This configuration of the use of .start(), and .join()
#will run your threads SERIALY.

----
t1 = threading.Thread(target=self.print_evens)
t2 = threading.Thread(target=self.print_odds)

t1.start()
t1.join()

t2.start()
t2.join()
----"""
        )

        # This configuration of .start() and .join() will run threads concurrently
        t1.start()
        t1.join()

        t2.start()
        t2.join()
        print(
            """This print statement is called at the end of the main thread, notice 
that when calling .join() on a worker thread this blocks the main thread until
the worker thread has finished its task.  It is this blocking property that enables this configuration
of threads to run SERIALLY. This print statement is the last executed code in the main thread"""
        )

    def daemon_concurrent_example(self):
        t1 = threading.Thread(daemon=True, target=self.print_evens)
        t2 = threading.Thread(daemon=True, target=self.print_odds)

        print(
            """
#This is a DAEMON CONCURRENT thread example.
#You will see that odd and even numbers will print
#in mixed order as the threads run concurrently.
#This configuration of the use of .start(), and .join()
#will run your threads concurrently.

----
t1 = threading.Thread(daemon=True,target=self.print_evens)
t2 = threading.Thread(daemon=True,target=self.print_odds)

t1.start()
t2.start()

t1.join()
t2.join()
----

"""
        )

        # This configuration of .start() and .join() will run threads concurrently
        t1.start()
        t2.start()

        t1.join()
        t2.join()
        print(
            """This print statement is called at the end of the main thread, notice 
that just as in the 'non-daemon' worker thread case, when calling .join() on a worker 
thread this blocks the main thread until the worker thread has finished its task.  
This print statement is the last executed code in the main thread.

Run the non .join() 'Daemon' example to find a difference between 'Daemon' and 'Non-Daemon' worker threads. """
        )

    def daemon_no_join_concurrent_example(self):
        t1 = threading.Thread(daemon=True, target=self.print_evens)
        t2 = threading.Thread(daemon=True, target=self.print_odds)

        print(
            """
#This is a DAEMON CONCURRENT 'no .join()' thread example.
#You might expect that odd and even numbers will print concurrently...

----
t1 = threading.Thread(daemon=True,target=self.print_evens)
t2 = threading.Thread(daemon=True,target=self.print_odds)

t1.start()
t2.start()

----

"""
        )

        # This configuration of .start() will run threads concurrently if your main thread doesn't exit.
        t1.start()
        t2.start()

        print(
            """This print statement is called at the end of the main thread, notice 
that in this 'daemon' worker thread case example no numbers are output.  This is because
a daemon thread without a call to .join() will not be waited for by the main thread.
The main thread printed this statement, exited, and the worker thread didn't
get a chance to complete its job.  Ofcourse, if the main thread is kept alive
by some other task your daemon threads might stand a chance at doing their jobs concurrently.
"""
        )
