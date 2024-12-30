#    Main Author(s): Ali Riza Sevgili, Canberk Secilmez
#    Main Reviewer(s): Ali Riza Sevgili, Canberk Secilmez
 

class SortedList:
    class Node:
        def __init__(self, data=None, next_node=None, prev_node=None):
            self.data = data
            self.next = next_node
            self.prev = prev_node    

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get_front(self):
        if self.is_empty():
            return None
        return self.head

    def get_back(self):
        if self.is_empty():
            return None
        return self.tail

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.count

    def insert(self, data):
        new_node = self.Node(data)
        
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            
            current = self.head
            while current is not None and current.get_data() < data:
                current = current.get_next()

            if current is None:
                
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            elif current == self.head:
                
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
              
                previous_node = current.get_previous()
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current
                current.prev = new_node

        self.count += 1
        return new_node

    def erase(self, node):
        if node is None:
            raise ValueError('Cannot erase node referred to by None')
        
        if node == self.head:
            self.head = node.get_next()
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = node.get_previous()
            if self.tail:
                self.tail.next = None
        else:
            prev_node = node.get_previous()
            next_node = node.get_next()
            prev_node.next = next_node
            next_node.prev = prev_node

        self.count -= 1

    def search(self, data):
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return current
            current = current.get_next()
        return None

