import threading


def first_thread():
    print("This is the first thread running")

def second_thread():
    print("This is the second thread running")

def third_thread():
    print("Hi, I'm the third thread")

# Create threads for each run
thread1 = threading.Thread(target=first_thread)
thread2 = threading.Thread(target=second_thread)
thread3 = threading.Thread(target=third_thread)

# Start the threads to execute the tasks concurrently
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

# Once all threads have finished, output the message!
print("All threads execution has been completed!")