from LinkedList import LinkedList


class DisjointSet:

    def __init__(self):
        self.sets = []

    def __str__(self):
        text = '{ '
        for linked_list in self.sets:
            text += str(linked_list)
        text += ' }'
        return text

    def union(self, x, y):

        listax = self.getListWithRep(self.findSet(x))
        listay = self.getListWithRep(self.findSet(y))

        if listax is not None and listay is not None:
            val = listay.head.nextval

            while val is not None:
                val.refhead = listax.head.nextval
                val = val.nextval

            listax.tail.nextval = listay.head.nextval
            listax.tail = listay.tail
            self.sets.remove(listay)

        else:
            return None

    def makeSet(self, x):
        linked_list = LinkedList()
        linked_list.insert(x)
        self.sets.append(linked_list)

    def getListWithRep(self, representative):
        for linked_list in self.sets:
            if linked_list.getRepresentative() == representative:
                return linked_list
        return None

    def findSet(self, value):
        for linked_list in self.sets:
            nodo = linked_list.head.nextval
            while nodo is not None:
                if nodo.dataval == value:
                    return linked_list.getRepresentative()
                nodo = nodo.nextval
        return None
