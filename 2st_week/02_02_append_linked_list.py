class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList의 가장 끝에 있는 노드에 새로운 노드 연결
    def append(self, value):
        cur = self.head

        # next가 있는 때까지 cur를 뒤로 옮기는 작업을 반복
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    # LinkedList에 저장한 head를 따라가면서 모든 노드를 전부 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(5)
linked_list.append(10)
linked_list.append(15)
linked_list.print_all()