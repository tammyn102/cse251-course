"""
Course: CSE 251
Lesson Week: 10
File: assignment.py
Author: Tammy Nolasco

Purpose: assignment for week 10 - reader writer problem

Instructions:

- Review TODO comments

- writer: a process that will send numbers to the reader.  
  The values sent to the readers will be in consecutive order starting
  at value 1.  Each writer will use all of the sharedList buffer area
  (ie., BUFFER_SIZE memory positions)

- reader: a process that receive numbers sent by the writer.  The reader will
  accept values until indicated by the writer that there are no more values to
  process.  
  
- Display the numbers received by the reader printing them to the console.

- Create WRITERS writer processes

- Create READERS reader processes

- You can use sleep() statements for any process.

- You are able (should) to use lock(s) and semaphores(s).  When using locks, you can't
  use the arguments "block=False" or "timeout".  Your goal is to make your
  program as parallel as you can.  Over use of lock(s) or lock(s) in the wrong
  place will slow down your code.

- You must use ShareableList between the two processes.  This shareable list
  will contain different "sections".  There can only be one shareable list used
  between your processes.
  1) BUFFER_SIZE number of positions for data transfer. This buffer area must
     act like a queue - First In First Out.
  2) current value used by writers for consecutive order of values to send
  3) Any indexes that the processes need to keep track of the data queue
  4) Any other values you need for the assignment

- Not allowed to use Queue(), Pipe(), List() or any other data structure.

- Not allowed to use Value() or Array() or any other shared data type from 
  the multiprocessing package.

Add any comments for me:

"""
from asyncio.subprocess import Process
import random
from multiprocessing.managers import SharedMemoryManager
import multiprocessing as mp
import time

BUFFER_SIZE = 10
READERS = 2
WRITERS = 2

class ReaderWriter():
    def __init__(self):
        self.rd = mp.Pool.Semaphore()

    def reader(self):
          while True:
            self.rd.acquire()  
            if self.readCount == 1:
                  self.wrt.acquire()
                  print(f"Reader {self.readCount} is reading")
                  self.rd.acquire() 
            if self.readCount == 0:      
               self.wrt.release()

    def writer(self):
          while True:
                self.wrt.acquire()     
                print("Wrting data.....")  
                print("-"*20)
                self.wrt.release()   
                time.sleep(3)    
def main(self):

    # This is the number of values that the writer will send to the reader
    items_to_send = random.randint(1000, 10000)

    smm = SharedMemoryManager()
    smm.start()

    sl = smm.ShareableList(range(BUFFER_SIZE))

    # TODO - Create a ShareableList to be used between the processes
    # TODO - Create any lock(s) or semaphore(s) that you feel you need
    # TODO - create reader and writer processes
    # TODO - Start the processes and wait for them to finish
    t1 = Process(target = self.reader) 
    t1.start()
    t2 = Process(target = self.writer) 
    t2.start()
    t3 = Process(target = self.reader) 
    t3.start()
    t4 = Process(target = self.reader) 
    t4.start()
    t6 = Process(target = self.writer) 
    t6.start()
    t5 = Process(target = self.reader) 
    t5.start()
    print(f'{items_to_send} values sent')

    # TODO - Display the number of numbers/items received by the reader.
    #        Can not use "items_to_send", must be a value collected
    #        by the reader processes.
    # print(f'{<your variable>} values received')

    smm.shutdown()
    total_result = sum(sl)

if __name__ == '__main__':
    main()
