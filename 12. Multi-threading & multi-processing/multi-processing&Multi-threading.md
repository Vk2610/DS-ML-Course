# Multi - threading & multi-processing

## Understand the core concepts

1. `Program`: A program is a set of instructions that performs a specific task when executed. It is a static entity that resides on disk and can be executed multiple times.

- Example: A Python script that calculates the factorial of a number is a program. It can be executed multiple times with different input values.

2. `Process`: A process is an instance of a program that is currently being executed. It has its own memory space, system resources, and execution context. Each process runs independently and can have multiple threads.

- Example: When you run a Python script, it creates a process. If you run the same script again, it creates another process. Each process has its own memory and resources.

3. `Thread`: A thread is the smallest unit of execution within a process. It shares the same memory space and resources as other threads in the same process. Threads allow for concurrent execution of tasks within a process.

i. `Single Threaded Process` : A single-threaded process has only one thread of execution. It can only perform one task at a time. If the thread is busy executing a task, it cannot perform any other tasks until it finishes.

ii. `Multi-threaded Process` : A multi-threaded process has multiple threads of execution. It can perform multiple tasks concurrently, allowing for better performance and responsiveness.

- Example: In a web browser, each tab can be a separate thread. This allows you to browse multiple websites simultaneously without affecting the performance of the browser.

## Strcuture of process

A process typically consists of the following components:

1. `Code`: The executable instructions of the program.
2. `Data`: The variables and data structures used by the program.
3. `Stack`: The memory area used for function calls and local variables.
4. `Heap`: The memory area used for dynamic memory allocation.
5. `Program Counter`: A register that keeps track of the current instruction being executed.
6. `Process Control Block (PCB)`: A data structure that contains information about the process
   such as its state, priority, and resources allocated to it.

## Diagram

---

## | Stack | ← grows downward

## | Heap | ← grows upward

## | Uninitialized Data |

## | Initialized Data |

## | Text (Code) |

## Conclusion

In summary, a program is a static set of instructions, while a process is an instance of a program that is currently being executed. A process can have multiple threads, which allow for concurrent execution of tasks within the process. Understanding these concepts is crucial for developing efficient and responsive applications.
