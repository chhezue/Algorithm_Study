class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next

    # index번째 원소 반환
    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index is not index:
            cur = cur.next
            cur_index += 1

        return cur

    # index 위치에 노드 저장
    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index - 1) # 이전 노드 필요
        next_node = prev_node.next # new_node의 next가 될 노드

        new_node.next = next_node
        prev_node.next = new_node

    # index 위치의 노드 삭제
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        cur_node = self.get_node(index)
        prev_node = self.get_node(index - 1)
        next_node = cur_node.next

        prev_node.next = next_node
        cur_node.next = None

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1, 6)
linked_list.add_node(0, 7)
linked_list.delete_node(0)

linked_list.print_all()