class Node:
    def __init__(self,value=None,next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self,new_value):
        self._value = new_value

    def setNext(self,new_next):
        self._next = new_next

class LinkedList:
    def __init__(self):     # 初始化链表为空表
        self._head = None
        self._tail = None
        self._length = 0

    def size(self):
        return self._length

    def isEmpty(self):
        return self._head == None

    # 在链表前端添加元素：O(1)
    def add(self,value):
        newnode = Node(value)
        newnode.setNext(self._head)
        self._head = newnode

    # 在链表尾部添加元素：O(n)
    def append(self,value):
        newnode = Node(value)
        if self.isEmpty():
            self._head = newnode
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newnode)

    def search(self,value):
        current = self._head
        found = False
        while current != None and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        return found

    # 索引元素在链表中的位置
    def index(self,value):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError('%s is not in the linkedlist' %value)

    def remove(self,value):
        current = self._head
        pre = None
        while current != None:
            if current.getValue() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    def insert(self,pos,value):
        if pos <= 1:
            self.add(value)
        elif pos > self.size():
            self.append(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

