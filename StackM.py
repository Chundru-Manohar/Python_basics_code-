import collections
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(30)
stack.append(50)
print(stack)
stack.pop()
stack.pop()
stack.pop()
print(stack)
print(not stack)
print(len(stack)==0)

import queue
dm = queue.LifoQueue()
dm.put(20)
dm.put(50)

print("ravi")