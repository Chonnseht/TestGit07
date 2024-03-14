from queue import LifoQueue

def run_stack():
    # Initializing
    stack = LifoQueue(maxsize=3)
    stack.put(11) # Python built-in use "put" for Push
    stack.put(12)
    stack.put(13)

    if stack.full():
        print("Full")
    else:
        print("Not full")

    print("Now, pop the element out of Stack")

    print(stack.get()) # Python built-in use "Get" for Dequeue

    if stack.full():
        print("Full")
    else:
        print("Not full")

    print(stack.get())
    print(stack.get())

    if stack.empty():
        print("Empty")
    else:
        print("Not empty")

    print('Number of elements in a stack:' + str(stack.qsize()))

def run():
    run_stack()