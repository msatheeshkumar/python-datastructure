from Node import Node

class UnorderedList:


    def __init__(self):
		self.head = Node(0)
		self.addedFirst = None

    def isEmpty(self):
        self.head.getNext() == None

    def add(self, item):
        temp = Node(item)
        headNode = self.head

        while headNode.next != None:
            headNode = headNode.next

        headNode.next = temp
        self.head.data = self.head.data + 1

    def size(self):
        count = self.head.data
        return count

    def remove(self, item):
        current = self.head.next
        previous = None
        found = False
        while not found and current != None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head.data = self.head.data - 1
            self.head.next = current.next
        elif found == True and current.next == None:
            self.head.data = self.head.data - 1
            previous.next = None
        elif found == True and previous != None:
            self.head.data = self.head.data - 1
            previous.next = current.next
        else:
            print('%d is not found in the list' %item)

    def printLL(self):
        current = self.head.next
        while current != None:
            print current.data
            current = current.next


llist = UnorderedList()
llist.add(31)
llist.add(77)
llist.add(17)
llist.add(93)
llist.add(26)
llist.add(54)

llist.remove(31)

llist.printLL()

print(llist.size())

