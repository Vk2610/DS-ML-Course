# Multi-Processing 
# Multi-processing is a technique that allows a program to run multiple processes concurrently, each with its own memory space. This is particularly useful for CPU-bound tasks, as it can take advantage of multiple CPU cores to improve performance.

# When to multi-process:
# 1. CPU-bound tasks: If your program is performing tasks that require a lot of CPU time, such as heavy computations or data processing, multi-processing can help speed up the execution by utilizing multiple CPU cores.

# 2. Independent tasks: If your program has tasks that can be executed independently without sharing data, multi-processing can be a good choice. Each process can run its own task without worrying about synchronization issues.

# 3. Avoiding GIL: In Python, the Global Interpreter Lock (GIL) can limit the performance of multi-threading for CPU-bound tasks. Multi-processing can bypass the GIL by creating separate processes, allowing for true parallelism.

import multiprocessing
import time

def square_number(n):
    print(f"Square of {n} is {n * n}")
    time.sleep(1)  # Simulate a time-consuming task

def cube_number(n):
    print(f"Cube of {n} is {n * n * n}")
    time.sleep(1)  # Simulate a time-consuming task

if __name__ == "__main__":

    # create 2 processes for the tasks
    p1 = multiprocessing.Process(target=square_number, args=(5,))
    p2 = multiprocessing.Process(target=cube_number, args=(5,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()

    print("Both processes have finished execution.")