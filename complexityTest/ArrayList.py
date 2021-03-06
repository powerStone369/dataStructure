import ctypes

class ArrayList:
  def __init__(self):
    self._n = 0
    self._capacity = 1
    self._A = self._make_array(self._capacity)
    
  def __len__(self):
    return self._n
    
  def __getitem__(self, k):
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]
  
  def append(self, obj):
    if self._n == self._capacity:
      self._resize(2 * self._capacity)
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):
    B = self._make_array(c)
    for k in range(self._n):
      B[k] = self._A[k]
    self._A = B
    self._capacity = c

  def _make_array(self, c):
     return (c * ctypes.py_object)() 

  def insert(self, k, value):
    if k < 0:
      raise IndexError('index must be equal or greater than 0')
    if k > self._n:
      k = self._n
    if self._n == self._capacity:
      self._resize(2 * self._capacity)
    for j in range(self._n, k, -1):
      self._A[j] = self._A[j-1]
    self._A[k] = value
    self._n += 1

  def remove(self, k):
    if self._n == 0:
      raise ValueError('list is empty')
    if k > self._n:
      k = self._n - 1
    result = self._A[k]
    for j in range(k, self._n - 1):
      self._A[j] = self._A[j+1]
    self._n -= 1
    return result