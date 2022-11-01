from collections import deque #optimized for add/remove from both ends of collection

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

x = queue.popleft() #popleft
print(x)
print(queue)