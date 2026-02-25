### Multiprocessing with Process Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time
def square_number(n):
    time.sleep(1)  # Simulate a time-consuming task
    return n * n
  
numbers = [1, 2, 3, 4, 5]

with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(square_number, numbers)

print(list(results))