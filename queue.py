# circular array-based Queue implementation

class ArrayQueue:
  DEFAULT_CAPACITY = 10
  # initialize member variables:
  # _size: count elements in queue
  # _front: pointer for first item
  # _rear: (optional) pointer for last item

  def __init__(self):
   
    self._data = [None] * self.DEFAULT_CAPACITY
    self._front = 0
    self._rear = -1
    self._size = 0

  def __len__(self):

    return self._size

  def is_empty(self):
    
    return self._size == 0

  def first(self):
    
    return self._data[self._front]

  def last(self):
    
    return self._data[self._rear]

  def enqueue(self, e):

    if self._size >= 10:
      print("큐의 사이즈가 10을 초과하였습니다")
    
    else:
     self._rear = (self._rear+1) % self.DEFAULT_CAPACITY
     self._size += 1
     self._data[self._rear] = e


  def dequeue(self):
    if self._size == 0 :
      print("Queue is empty")      
    else:
      temp = self._data[self._front]
      self._data[self._front] = [None]
      self._size -= 1
      self._front = (self._front + 1) % self.DEFAULT_CAPACITY
      return temp

#################Test code#######################

t = ArrayQueue()
print("큐에 1,2,3 enqueue")
t.enqueue(1)
t.enqueue(2)
t.enqueue(3)

print("first값")
print(t.first())
print("last 값")
print(t.last())

print("dequeue 수행")
t.dequeue()

print("first값")
print(t.first())
print("last 값")
print(t.last())
