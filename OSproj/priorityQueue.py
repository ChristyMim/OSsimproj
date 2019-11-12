class Node:
    def __init__(self, data, priority):
        self.data = data
        self.next = None
        self.priority = priority


class Priority_Queue:

    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data, priority):
        #temp = self.head
        #new_node = Node(data, priority)

        # if self.last is None:
        #     self.head = Node(data, priority)
        #     self.last = self.head
        # else:
        #     self.last.next = Node(data, priority)
        #     self.last = self.last.next

        current = self.head

        if current is None:
            new_node = Node(data)
            self.head = new_node
            return

        if current.data > data:
            new_node = Node(data)
            new_node.next = current
            self.head = new_node
            return

        while current.next is not None:
            if current.next.data > data:
                break
            current = current.next

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def first(self):
        return self.head.data

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def print_priority(self):
        print("priority queue elements are:")
        count = 1
        temp = self.head

        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
            if count % 10 == 0:
                print('\n')
            count += 1
