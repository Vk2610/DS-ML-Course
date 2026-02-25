#  Multi threading
# When to use multi threading:
# 1. When you have a task that can be broken down into smaller tasks that can be executed concurrently.
# 2. When you have a task that is I/O bound, such as reading from a file or making a network request.
# 3. When you want to improve the performance of your application by utilizing multiple CPU cores, but you don't want to deal with the complexities of multi processing.


import threading 
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)
        
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start() 