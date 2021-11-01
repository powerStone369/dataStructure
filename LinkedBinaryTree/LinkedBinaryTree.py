class Tree:
  class Position:
    def element(self):
      raise NotImplementedError('must be implemented')
    def __eq__(self, other):
      raise NotImplementedError('must be implemented')
    def __ne__(self, other):
      return not (self == other)

  def root(self):
    raise NotImplementedError('must be implemented')
  def parent(self, p):
    raise NotImplementedError('must be implemented')
  def num_children(self, p):
    raise NotImplementedError('must be implemented')
  def children(self, p):
    raise NotImplementedError('must be implemented')
  def __len__(self):
    raise NotImplementedError('must be implemented')

## true/false 값을 return
  def is_root(self, p):
    return self.root() == p
  def is_leaf(self, p):
    return self.num_children(p) == 0
  def is_empty(self):
    return len(self) == 0

#현재 노드로부터 root까지 길이 -> 부모노드로 가면서 1씩 계속 더해준다. 루트 갈때까지. 
  def depth(self, p):
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))

#모든포지션중에서 leaf골라서 depth가 가장 깊은것 리턴
  def _height1(self):
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    

#자녀노드들 중 높이가 가장 큰것 + 1
  def _height2(self, p):
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height2(c) for c in self.children(p))

  
  def height(self, p=None):
    if p is None:
      p = self.root()
    return self._height2(p)

  def preorder(self):
    if not self.is_empty():
      for p in self._subtree_preorder(self.root()):
        print("프리오더p 앞까지옴")
        yield p
        print("프리오더p 뒤까지옴")

  def _subtree_preorder(self, p):
    print("서브트리p 앞까지옴")
    yield p
    print("서브트리p 뒤")
    for c in self.children(p):
      print("칠드런들어감")
      for other in self._subtree_preorder(c):
        print("other 앞까지옴")
        yield other
        print("other 뒤임")


  def inorder(self): # homework!
    if not self.is_empty():
      for p in self._subtree_inorder(self.root()):       
        yield p
        

  def _subtree_inorder(self, p): # homework! 
      for c in self.children(p):
        #1 자기노드를 방문하기 위한 조건문. 왼쪽 자식노드로 가지 않을경우 yield p 해준다 (혼자서는 완벽하지 않으므로 #3를 꼭 붙여줘야 한다)
        if c != self.left(p) :
          yield p   
        for other in self._subtree_inorder(c): 
          yield other
       #2 리프노드에서 p yield를 해준다. 순서는 #1에서 처리하였음
      if self.is_leaf(p) == True:
       yield p  
       #3 #1에서 우측 자식노드가 없는경우에는 #1을 실행하지 못하므로 그경우를 대비해 우측 자식노드가 없을때 자기노드를 yield해준다 
      elif self.right(p) == None:
       yield p   
     

    
  

  def positions(self): 
    return self.inorder()


class BinaryTree(Tree):
  def left(self, p):
    raise NotImplementedError('must be implemented')
  def right(self, p):
    raise NotImplementedError('must be implemented')
    
  def sibling(self, p):
    parent = self.parent(p)
    if parent is None:
      return None
    else:
      if p == self.left(parent):
        return self.right(parent)
      else:
        return self.left(parent)
  def children(self, p):
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)


class LinkedBinaryTree(BinaryTree):
  class _Node:
    __slots__ = ('_element', '_parent', '_left', '_right')
    def __init__(self, element, parent=None, left=None, right=None):
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right

  class Position(BinaryTree.Position):
    def __init__(self, container, node):
      self._container = container
      self._node = node

    def element(self):
      return self._node._element
    def __eq__(self, other):
      return type(other) is type(self) and other._node is self._node
    
  def _validate(self, p):
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._parent is p._node:
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    return self.Position(self, node) if node is not None else None

  def __init__(self):
    self._root = None
    self._size = 0

  def __len__(self):
    return self._size
  def root(self):
    return self._make_position(self._root)
  def parent(self, p):
    node = self._validate(p)
    return self._make_position(node._parent)
  
  def left(self, p):
    node = self._validate(p)
    return self._make_position(node._left)
  def right(self, p):
    node = self._validate(p)
    return self._make_position(node._right)

  def num_children(self, p):
    node = self._validate(p)
    count = 0
    if node._left is not None:
      count += 1
    if node._right is not None:
      count += 1
    return count

  def _add_root(self, e):
    if self._root is not None:
      raise ValueError('Root already exists')
    self._size = 1
    self._root = self._Node(e)
    return self._make_position(self._root)

  def _add_left(self, p, e):
    node = self._validate(p)
    if node._left is not None:
      raise ValueError('Left child already exists')
    self._size += 1
    node._left = self._Node(e, node)
    return self._make_position(node._left)

  def _add_right(self, p, e):
    node = self._validate(p)
    if node._right is not None:
      raise ValueError('Right child already exists')
    self._size += 1
    node._right = self._Node(e, node)
    return self._make_position(node._right)

  def _replace(self, p ,e):
    node = self._validate(p)
    old = node._element
    node._element = e
    return old

  def _delete(self, p):
    node = self._validate(p)
    if self.num_children(p) == 2:
      raise ValueError('p has two children')
    child = node._left if node._left else node._right
    if child is not None:
      child._parent = node._parent
    if node is self._root:
      self._root = child
    else:
      parent = node._parent
      if node is parent._left:
        parent._left = child
      else:
        parent._right = child
    self._size -= 1
    node._parent = node
    return node._element

  def _attach(self, p, t1, t2):
    node = self._validate(p)
    if not self.is_leaf(p):
      raise ValueError('p is not a leaf')
    if not type(self) is type(t1) is type(t2):
      raise TypeError('Type must match')
    self._size += len(t1) + len(t2)
    if not t1.is_empty():
      t1._root._parent = node
      node._left = t1._root
      t1._root = None
      t1._size = 0
    if not t2.is_empty():
      t2._root._parent = node
      node._left = t2._root
      t2._root = None
      t2._size = 0
