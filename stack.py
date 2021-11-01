class Stack:

    def __init__ (self):
        self._data = []

    #Push
    def push (self, item):
        self._data.append(item)

    #Pop
    def pop(self):

        if not self.isEmpty():
            return self._data.pop(-1)
        else:
            print("Stack is Empty")
            
    #Is Empty
    def isEmpty(self):
        return len(self._data)==0
 
    #Top
    def top(self):
        if not self.isEmpty():
            return self._data[-1]
        else:
            print("Stack is Empty")

    #Size
    def size(self):
        return len(self._data)
    
    
#################Test code#######################

t = Stack()

print("스택에 1,2 push")
t.push(1)
t.push(2)

print("top 출력")
print(t.top())

print("pop 수행 후 top 출력")
t.pop()
print(t.top())
    
    