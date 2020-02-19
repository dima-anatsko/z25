"""
1*. Переписать код из homework6 используя ООП
2. Реализовать класс "очередь"
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
- в качестве инициализации принимает размер очереди, если параметр не указан,
то очередь - бесконечная
- выдать сообщение об ошибке, если в полную очередь добавить элемент нельзя,
или из пустой очереди достать элемент
3. Реализовать класс "стек"
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
- в качестве инициализации принимает размер стека, если параметр не указан,
то стек - бесконечный
- выдать сообщение об ошибке, если в полный стек добавить элемент нельзя,
или из пустого стека достать элемент
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self, size=None):
        self.size = size
        self._head = None
        self._tail = None
        self.count = 0

    def _check_size(self):
        if self.size is not None and self.size == self.count:
            raise Exception("Overflow")

    def _check_remove(self):
        if self.count == 0:
            raise Exception("Object is empty")

    def _first_item(self, new_node):
        self._head = new_node
        self._tail = new_node

    @property
    def peek(self):
        if self._tail:
            return self._tail.value
        else:
            raise Exception("Object is empty")

    def push(self, value):
        self._check_size()
        new_node = Node(value)
        if self._head is None:
            self._first_item(new_node)
        else:
            last_node = self._tail
            self._tail = new_node
            last_node.next = new_node
            new_node.previous = last_node
        self.count += 1

    def remove_to_end(self):
        self._check_remove()
        last_node = self._tail
        self._tail = last_node.previous
        if self._tail:
            self._tail._next = None
        else:
            self._head = None
        self.count -= 1
        return last_node.value

    def remove_to_start(self):
        self._check_remove()
        first_node = self._head
        self._head = first_node.next
        if self._head:
            self._head.previous = None
        else:
            self._tail = None
        self.count -= 1
        return first_node.value


class Stack(LinkedList):
    @property
    def pop(self):
        return super().remove_to_end()


class Queue(LinkedList):
    @property
    def pop(self):
        return super().remove_to_start()

    @property
    def peek(self):
        if self._head:
            return self._head.value
        else:
            raise Exception("Object is empty")


a = Queue()
_list = [x * 2 for x in range(10)]
for i in _list:
    a.push(i)
print(a.peek)
print(a.pop)
print(a.pop)
print(a.peek)
a.push(44)
print(a.peek)
print(a.count)
