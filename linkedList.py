
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def printNext(self):
        print(self.next)

    def printData(self):
        print(self.data)


class linkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        nodes = self.head
        while( nodes != None):
            print(nodes.data)
            nodes = nodes.next

    def length(self):

        length = 0
        nodes = self.head
        while(nodes != None):
            nodes = nodes.next
            length = length + 1

        return length

    def append(self, newData):
        newNode = Node(newData)

        temp = self.head
        if temp == None:
            self.head = newNode
        else:
            node = self.head
            while( node.next != None ):
                node = node.next
            node.next = newNode

    def prepend(self, newData):
        newNode = Node(newData)

        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert(self, index, newData):
        newNode = Node(newData)

        nodes = self.head
        round = 1
        while(nodes != None and round < index):
            if(round == index - 1):
                tempNext = nodes.next
                nodes.next = newNode
                newNode.next = tempNext

            nodes = nodes.next
            round = round + 1

    def getElementAtIndex(self, index):

        nodes = self.head
        round = 1
        while(nodes != None and round <= index):
            if(round == index):
                return nodes.data

            nodes = nodes.next
            round = round + 1



list = linkedList()
list.append(1)
list.prepend(2)
list.append(3)
list.prepend(4)
list.insert(2, 5)

list.printList()
print "the length of the linked list is {}" .format (list.length())
print "the data of the 2th node is {}".format (list.getElementAtIndex(2))
