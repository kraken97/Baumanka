import queue


def test_queue(cls):
    q = cls()
    print(" Empty queue test")
    assert q.dequeue() == None
    print(" Add elements and then get them will give equal values")
    for i in range(1, 20):
        q.enqueue(i)
    for i in range(1, 20):
        assert q.dequeue() == i
    print(" Assert queue is empty")"
    assert q.dequeue() == None

    print("Test adding and removing in one time")
    print("Added 40 elements, deleted 20, 20 left")
    for i in range(20):
        q.enqueue(i * 2)
        q.enqueue(i * 2 + 1)
        q.dequeue()
    for i in range(20, 40):
        assert q.dequeue() == i


class MyQueue(queue.Queue):
    def enqueue(self, el):
        self.put(el)

    def dequeue(self):
        res = None
        try:
            res = self.get_nowait()
        except queue.Empty:
            res = None
        return res


test_queue(MyQueue)
