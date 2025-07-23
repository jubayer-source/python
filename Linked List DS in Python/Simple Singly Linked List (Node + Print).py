class Node:
    def __init__(self, data):
        self.data = data  # Node er value
        self.next = None  # Next node er reference

# 3 ta node banacchi
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Node gulo ke link korchi
node1.next = node2
node2.next = node3

# Print korar function
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

print_linked_list(node1)
