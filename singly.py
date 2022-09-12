class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            h = self.head
            while h.next != None:
                h = h.next
            h.next = Node(item)
        self._size += 1

    def addHead(self, item):
        h = Node(item)
        h.next = self.head
        self.head = h
        self._size += 1

    def search(self, item):
        if self._size != 0:
            h = self.head
            for i in range(self._size):
                if h.value == item:
                    return 'Found'
                h = h.next
            return 'Not Found'
        else:
            return 'Not Found'

    def index(self, item):
        count = 0
        h = self.head
        if self._size != 0:
            for i in range(self._size):
                if h.value == item:
                    return count
                count += 1
                h = h.next
            return -1
        else:
            return -1

    def size(self):
        return self._size

    def pop(self, pos):
        if self._size == 0:
            return 'Out of Range'
        if pos == 0:
            self.head = self.head.next
        if abs(pos) > self._size:
            return 'Out of Range'
        if pos < 0:
            pos = (self._size - 1) + pos
        if pos > 0:
            h = self.head
            for i in range(pos-1):
                h = h.next
            h.next = h.next.next
        return 'Success'


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)