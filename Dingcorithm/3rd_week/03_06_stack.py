class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value) # [3] 노드 생성
        new_head.next = self.head # [3] 노드 뒤에 현재 헤드 연결: [3] -> [4]
        self.head = new_head # 현재 링크드리스트의 헤드를 new_head로 변경

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        deleted_head = self.head
        self.head = self.head.next
        return deleted_head.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        return self.head.data

    def is_empty(self):
        if self.head is None:
            return True
        return False