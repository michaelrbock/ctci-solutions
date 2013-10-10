class Node:
	def __init__(self):
		self.adjacent = []
		self.visited = False

class Queue:
	def __init__(self):
		self._queue = []

	def enqueue(self, node):
		self._queue.append(node)

	def dequeue(self):
		if self._queue:
			return self._queue.pop(0)
		return None

	def is_empty(self):
		return len(self._queue) == 0

def is_path(start, end):
	queue = Queue()
	queue.enqueue(start)
	start.visited = True
	while not queue.is_empty():
		current = queue.dequeue()
		if current == end:
			return True
		for node in current.adjacent:
			if not node.visited:
				node.visited = True
				queue.enqueue(node)
	return False
