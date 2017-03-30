from collections import deque

queue = deque(["Jim", "John", "Lucy"])
queue.append("Lily")           # Lily 入队
print(queue)
#输出: deque(['Jim', 'John', 'Lucy', 'Lily'])
queue.append("Lilei")          # Lilei 入队

who = queue.popleft()                 # 队首元素出队
print(who)
#输出: Jim
queue.popleft()                 # 队首元素出队
print(queue)
#输出: deque(['Lucy', 'Lily', 'Lilei'])
