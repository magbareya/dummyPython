import threading
import time

c = 0
# Define a function for the thread
def print_time( threadName, delay):
	global c
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s: %s"%( threadName, time.ctime(time.time()) ))
	c = c+1

# Create two threads as follows
try:
	t1 = threading.Thread(target=print_time, args=("Thread-1", 2, ))
	t2 = threading.Thread(target=print_time, args=("Thread-2", 4, ))
	t1.start()
	t2.start()
except ValueError:
	print("Error: unable to start thread")
	print(ValueError)

while c < 2:
	pass