from queue import Queue

def run():
    # Initializing
    q = Queue(maxsize=3)

    q.put(11) # Python built-in use "put" for Enqueue
    q.put(12)
    q.put(13)

    if q.full():
        print("Full")
    else:
        print("Not full")

    print("Now, Dequeue the element out of Queue")

    print(q.get()) # Python built-in use "get" for Dequeue

    if q.full():
        print("Full")
    else:
        print("Not full")

    print(q.get())
    print(q.get())

    if q.empty():
        print("Empty")
    else:
        print("Not empty")

    print('Number of elements in a queue:' + str(q.qsize()))