"""
Course: CSE 251
Lesson Week: 11
File: Assignment.py
"""

import time
import random
import multiprocessing as mp

# number of cleaning staff and hotel guests
CLEANING_STAFF = 2
HOTEL_GUESTS = 5
cleaned_count = 0
party_count = 0


# Run program for this number of seconds
TIME = 60

STARTING_PARTY_MESSAGE =  'Turning on the lights for the party vvvvvvvvvvvvvv'
STOPPING_PARTY_MESSAGE  = 'Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^'

STARTING_CLEANING_MESSAGE =  'Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
STOPPING_CLEANING_MESSAGE  = 'Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'

# -----------------------------------------------------------------------------
def cleaner_waiting():
    time.sleep(random.uniform(0, 2))

# -----------------------------------------------------------------------------
def cleaner_cleaning(id):
    print(f'Cleaner {id}')
    time.sleep(random.uniform(0, 2))

# -----------------------------------------------------------------------------
def guest_waiting():
    time.sleep(random.uniform(0, 2))

# -----------------------------------------------------------------------------
def guest_partying(id):
    print(f'Guest {id}')
    time.sleep(random.uniform(0, 1))

# -----------------------------------------------------------------------------
def cleaner():
    """
    do the following for TIME seconds
    cleaner will wait to try to clean the room (cleaner_waiting())
    get access to the room
        display message STARTING_CLEANING_MESSAGE
        Take some time cleaning (cleaner_cleaning())
        display message STOPPING_CLEANING_MESSAGE
    """
    thread_list = []
    global time

    if CLEANING_STAFF == cleaner_waiting():
        return STARTING_PARTY_MESSAGE
        for guest_partying(id) in party_count:
            if guest_partying(TIME):
                 thread_list.append(threading.Thread(target=cleaner(), args=(guest_partying,)))
            else:
                return cleaner_cleaning(id)
    
    
# -----------------------------------------------------------------------------
def guest():
    """
    do the following for TIME seconds
    guest will wait to try to get access to the room (guest_waiting())
    get access to the room
        display message STARTING_PARTY_MESSAGE if this guest is the first one in the room
        Take some time partying (guest_partying())
        display message STOPPING_PARTY_MESSAGE if the guest is the last one leaving in the room
    """
    if HOTEL_GUESTS == guest_waiting():
        return STARTING_CLEANING_MESSAGE
        for cleaner_cleaning(id) in cleaned_count:
            if cleaner_cleaning(TIME):
                 thread_list.append(threading.Thread(target=guest(), args=(cleaner_cleaning,)))
            else:
                return guest_partying(id)

# -----------------------------------------------------------------------------
def main(thread_list):
    # TODO - add any variables, data structures, processes you need
    # TODO - add any arguments to cleaner() and guest() that you need

    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


    # Start time of the running of the program. 
    start_time = time.time()

    # Results
    print(f'Room was cleaned {cleaned_count} times, there were {party_count} parties')


if __name__ == '__main__':
    main()

