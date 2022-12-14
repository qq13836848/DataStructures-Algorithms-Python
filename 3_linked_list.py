# https://www.bilibili.com/video/BV1US4y1a72f
# to test these code, uncomment below bottom code


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):

        # if self.head is None:
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head

        while (temp.next):
            # or, while(temp.next is not None)
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None

        self.length -= 1
        # self.length = length - 1

        # remove the last Node
        if self.length == 0:
            self.head = None
            self.tail = None

        # get the Node removed
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # added a new Node to the list beginning
            new_node.next = self.head

            # to move head to the first Node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # if the linkedlist only have one Node
        # after call pop_first(), the length of linkedlist is zero
        # then set tail equal to None
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        # equal to "if index < 0 or index >= self.length: "
        if temp:
            # equal to "if temp is not None:"
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
            # if this remove() method is success, it will return a Node,
            # if not, it will return None
            # it is up to success return

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        # do not use "temp = temp.get(index)", because it's complexity is O(n)

        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


''' 
# bottom code

# test LinkedList.method

print('# create a LinkedList')
my_linked_list = LinkedList(1)
print('# test append(2), append(3), append(4)')
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print()
print()
print()
print()





print('# test pop()')
print('# to remove the last Node, do not care else')
my_linked_list.pop()

print('# to print the linkedlist right now')
my_linked_list.print_list()

print("\n# to remove the last Node, print it's object")
print(my_linked_list.pop())

print("\n# to remove the last Node, and get it's value")
print(my_linked_list.pop().value)

print('\n# to print the linkedlist right now')
my_linked_list.print_list()
print()
print()
print()
print()





print('# test prepend()')
my_linked_list.prepend(2)
my_linked_list.prepend(3)
my_linked_list.prepend(4)
print('# to print the linkedlist right now')
my_linked_list.print_list()
print()
print()
print()
print()





print('# test pop_first()')
print('# to remove the first Node, do not care else')
my_linked_list.pop_first()
print('# to print the linkedlist right now')
my_linked_list.print_list()
print()
print()
print()
print()




print('# test get(1)')
print(my_linked_list.get(1).value)
print()
print()
print()
print()




print('# test set_value(0, 23)')
my_linked_list.set_value(1, 23)
print('# to print the linkedlist right now')
my_linked_list.print_list()
print()
print()
print()
print()




print('# test insert(2, 76)')
my_linked_list.insert(2, 76)
print('# to print the linkedlist right now')
my_linked_list.print_list()
print()
print()
print()
print()







print('# test remove()')
my_linked_list.remove(0)
print('# to print the linkedlist right now')
my_linked_list.print_list()
print()
print()
print()
print()






print('# test reverse()')
print('# to reverse the linkedlist right now')
my_linked_list.reverse()
my_linked_list.print_list()

'''
