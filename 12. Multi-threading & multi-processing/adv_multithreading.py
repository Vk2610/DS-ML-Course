### Multi-threading with threading pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(1)  # Simulate a time-consuming task
    print(f"Numbers: {numbers}")
    
numbers=[1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, [numbers[i:i+2] for i in range(0, len(numbers), 2)])
    
print("All tasks have been completed.")


