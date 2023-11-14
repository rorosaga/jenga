from collections import deque


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, value):
        node = Node(value, self.top)
        self.top = node 
        
    def pop(self):
        if not self.top:
            return 
        
        value = self.top.value
        self.top = self.top.next
        return value


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
