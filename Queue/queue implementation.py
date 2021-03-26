# # FROM LIST
# queue=[]
# queue.append("A")
# queue.append("B")
# queue.append("C")
# queue.append("D")
# queue.append("E")
# print("Elements present in Queue")
# print(queue)
# print("\nElements dequeued in Queue")
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
# print("\n Queue after removing elements preaent:")
# print(queue)

#collection_deque
# from collections import deque
# q=deque()
# q.append("A")
# q.append("B")
# q.append("C")
# q.append("D")
# q.append("E")
# print("Elements present in Queue")
# print(q)
# print("\nElements dequeued in Queue")
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
# print("\n Queue after removing elements preaent:")
# print(q)

#queue_Queue
from queue import Queue
q=Queue(maxsize=4)
print(q.qsize())    #qsize() gives the maxsize of the queue
#Adding elements in the queue
q.put('A')
q.put('B')
q.put('C')
q.put('D')
print("\nFull: ",q.full()) #Return boolean for full
print("\n Elements dequeue in Queue:")
print(q.get())
print(q.get())
print(q.get())
print("\n Empty:",q.empty()) #Boolean for empty queue
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())


