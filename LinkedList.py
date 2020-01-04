class Node:

    def __init__(self, refhead=None, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.refhead = refhead


class LinkedList:

    def __init__(self):
        self.head = Node(None, 'S')
        self.tail = None

    def __str__(self):
        text = '{ '
        printval = self.head.nextval
        while printval is not None:
            text += str(printval.dataval) + ' '
            printval = printval.nextval
        text += '}'
        return text

    def insert(self, new_data):
        new_node = Node(self.head, new_data)

        if self.tail is None:
            self.head.nextval = new_node
            self.tail = new_node
        else:
            self.tail.nextval = new_node
            self.tail = new_node

    def getRepresentative(self):
        return self.head.nextval.dataval
