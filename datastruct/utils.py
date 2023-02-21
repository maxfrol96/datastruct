class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        pop_node = self.top
        pop_data = pop_node.data
        self.top = pop_node.next_node
        return pop_data

stack = Stack()
# stack.push('data1')
# stack.push('data2')
# stack.push('data3')
# print(stack.top.data)
# print(stack.top.next_node.data)
# print(stack.top.next_node.next_node.data)
# print(stack.top.next_node.next_node.next_node)
stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# теперь последний элемента содержит данные data1
print(stack.top.data)
print(data)