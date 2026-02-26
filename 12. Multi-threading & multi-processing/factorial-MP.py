'''
Real world Example : Multiprocessing for CPU-bound tasks
Scenario : Factorial calculation for a list of numbers
'''

import multiprocessing
import time
import sys
import math

def factorial(n):
    """Function to calculate factorial of a number"""
    return math.factorial(n)
if __name__ == "__main__":      
    numbers = [100000, 200000, 300000, 400000, 500000]  # List of numbers to calculate factorial
    start_time = time.time()  # Start time for multiprocessing

    # Create a pool of processes equal to the number of CPU cores
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorial, numbers)  # Map the factorial function to the list of numbers

    end_time = time.time()  # End time for multiprocessing
    print(f"Factorials: {results}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.2f} seconds")
    
    # For comparison, calculate factorials sequentially
    start_time_seq = time.time()  # Start time for sequential processing
    
    results_seq = [factorial(n) for n in numbers]  # Calculate factorials sequentially
    
    end_time_seq = time.time()  # End time for sequential processing
    print(f"Factorials (sequential): {results_seq}")
    print(f"Time taken sequentially: {end_time_seq - start_time_seq:.2f} seconds")  
    
    # Compare the speed difference between multiprocessing and sequential processing
    speedup = (end_time_seq - start_time_seq) / (end_time - start_time)
    print(f"Speedup: {speedup:.2f} times")