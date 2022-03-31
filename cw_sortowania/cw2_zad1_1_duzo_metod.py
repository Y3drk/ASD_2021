
'''class List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('cannot print empty list!')
            return

        current = self.head

        while current.next is not None:
            print(current.data, '- ', end='')
            current = current.next
        print(current.data)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print('cannot pop from empty list!')
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

def merge_lists(list_1, list_2):
    if list_1.head is None:
        return list_2
    elif list_2 is None:
        return list_1
    else:
        temp = List()

        while list_1.head is not None and list_2.head is not None:
            if list_1.head.data < list_2.head.data:
                temp.push(list_1.pop())
            else:
                temp.push(list_2.pop())

        while list_1.head is not None:
            temp.push(list_1.pop())

        while list_2.head is not None:
            temp.push(list_2.pop())

        result = List()
        while temp.head is not None:
            result.push(temp.pop())

    result.print()'''
