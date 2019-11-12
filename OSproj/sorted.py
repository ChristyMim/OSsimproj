class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class My_Sorted:

    def __init__(self):
        self.head = None

    def sort(self, data):
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

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def head(self):
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

    def print_list(self):
        print("sorted elements are:")
        count = 1
        temp = self.head

        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
            if count % 10 == 0:
                print('\n')
            count += 1
