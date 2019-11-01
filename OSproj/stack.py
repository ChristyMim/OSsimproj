class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class My_Stack:
    def __init__(self):
        self.head = None


    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def top(self):
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

    def printstack(self):
        print("stack elements are:")
        count = 1
        temp = self.head

        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
            if count % 10 == 0:
                print('\n')
            count += 1