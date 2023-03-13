class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList():
    def __init__(self, begin=None, end=None):
        self.begin = begin
        self.end = end

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.begin == None:
            self.begin = new_node
        else:
            new_node.next_node = self.begin
            self.begin = new_node
        if self.end == None:
            self.end = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.end == None:
            self.end = new_node
        else:
            self.end.next_node = new_node
            self.end = new_node
        if self.begin == None:
            self.begin = new_node

    def print_ll(self):
        ll_string = ''
        node = self.begin
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        linked_list_obj = []
        linked_list_data = []
        if self.begin != None:
            linked_list_obj.append(self.begin)
        else:
            return linked_list_data
        while True:
            if linked_list_obj[len(linked_list_obj)-1].next_node == None:
                break
            else:
                linked_list_obj.append(linked_list_obj[len(linked_list_obj)-1].next_node)
        for obj in linked_list_obj:
            linked_list_data.append(obj.data)
        return linked_list_data

    def get_data_by_id(self, id):
        try:
            linked_list_data = self.to_list()
            for data in linked_list_data:
                if data['id'] == id:
                    return data
        except TypeError:
            print(f'Данные не являются словарем или в словаре нет id {id}')

ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
print(ll.to_list())
user_data = ll.get_data_by_id(2)
print(user_data)

