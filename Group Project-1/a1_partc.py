#    Main Author(s): Canberk Secilmez, Ali Riza Sevgili

class Stack:

	def __init__(self, cap=10):
		self._capacity = cap
		self._size = 0
		self._data = [None] * cap

	def capacity(self):
		return self._capacity

	def push(self, data):
		if self._size >= self._capacity:
			new_capacity = self._capacity * 2
			new_data = [None] * new_capacity
			for i in range(self._size):
				new_data[i] = self._data[i]
			self._data = new_data
			self._capacity = new_capacity

		self._data[self._size] = data
		self._size += 1

	def pop(self):
		if self.is_empty():
			raise IndexError('pop() used on empty stack')
		top = self._data[self._size - 1]
		self._size -= 1
		return top

	def get_top(self):
		if not self.is_empty():
			return self._data[self._size - 1]
		return None

	def is_empty(self):
			return self._size == 0

	def __len__(self):
			return self._size


class Queue:


	def __init__(self, cap=10):
		self._capacity = cap
		self._size = 0
		self._data = [None] * cap
		self._front = 0
		self._back = 0

	def capacity(self):
		return self._capacity

	def enqueue(self, data):
		if self._size >= self._capacity:
			new_capacity = self._capacity * 2
			new_data = [None] * new_capacity
			for i in range(self._size):
				new_data[i] = self._data[(self._front + i) % self._capacity]
			self._data = new_data
			self._front = 0
			self._back = self._size
			self._capacity = new_capacity

		self._data[self._back] = data
		self._back = (self._back + 1) % self._capacity
		self._size += 1

	def dequeue(self):
		if self.is_empty():
			raise IndexError('dequeue() used on empty queue')
		front = self._data[self._front]
		self._front = (self._front + 1) % self._capacity
		self._size -= 1
		return front

	def get_front(self):
		if not self.is_empty():
			return self._data[self._front]
		return None

	def is_empty(self):
		return self._size == 0

	def __len__(self):
		return self._size



class Deque:

	def __init__(self, cap=10):
		self._capacity = cap
		self._size = 0
		self._data = [None] * cap
		self._front = 0
		self._back = 0

	def capacity(self):
		return self._capacity

	def push_front(self, data):
		if self._size >= self._capacity:
			new_capacity = self._capacity * 2
			new_data = [None] * new_capacity
			for i in range(self._size):
				new_data[i] = self._data[(self._front + i) % self._capacity]
			self._data = new_data
			self._front = 0
			self._back = self._size
			self._capacity = new_capacity

		self._front = (self._front - 1 + self._capacity) % self._capacity	
		self._data[self._front] = data
		self._size += 1

	def push_back(self, data):
		if self._size >= self._capacity:
			new_capacity = self._capacity * 2
			new_data = [None] * new_capacity
			for i in range(self._size):
				new_data[i] = self._data[(self._front + i) % self._capacity]
			self._data = new_data
			self._front = 0
			self._back = self._size
			self._capacity = new_capacity

		self._data[self._back] = data
		self._back = (self._back + 1) % self._capacity
		self._size += 1

	def pop_front(self):
		if self.is_empty():
			raise IndexError('pop_front() used on empty deque')
		front = self._data[self._front]
		self._front = (self._front + 1) % self._capacity
		self._size -= 1
		return front

	def pop_back(self):
		if self.is_empty():
			raise IndexError('pop_back() used on empty deque')
		self._back = (self._back - 1 + self._capacity) % self._capacity
		back = self._data[self._back]
		self._size -= 1
		return back

	def get_front(self):
		if self.is_empty():
			return None
		return self._data[self._front]

	def get_back(self):
		if self.is_empty():
			return None
		return self._data[(self._back - 1 + self._capacity) % self._capacity]

	def is_empty(self):
		return self._size == 0

	def __len__(self):
		return self._size

	def __getitem__(self, k):
		if k < 0 or k >= self._size:
			raise IndexError('Index out of range')
		return self._data[(self._front + k) % self._capacity]
