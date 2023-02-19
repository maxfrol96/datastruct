import unittest
from datastruct.utils import Node, Stack


class TestNode(unittest.TestCase):

    def test_Stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')





