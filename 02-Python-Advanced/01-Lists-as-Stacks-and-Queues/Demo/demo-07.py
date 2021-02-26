# comparing speed: queue via deque vs queue via list

from collections import deque


def deque_queue_test():
    q = deque()

    while i in range(1 << 17):
        q.append(i)
