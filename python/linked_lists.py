# Singly LinkedList 


class Node:
    def __init__(self, val = -1, next = None):
        self.val = val 
        self.next = next

class ListNode:
    def __init__(self, val = -1):
        self.next = None 
        self.prev = None 
        self.val = val 

class SinglyLinkedList:
    def __init__(self):
        self.head = self.tail = Node()

    def insert(self, val):
        self.tail.next = Node()
        self.tail = self.tail.next

    def remove(self, val):
        prev, curr = self.head, self.head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
                if curr == self.tail:  # Update tail if needed
                    self.tail = prev
                break
            prev, curr = curr, curr.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print("None")


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail 
        self.tail.prev = self.head
    
    def insert(self,val) -> ListNode:
        node = ListNode(val)
        self.tail.prev.next = node 
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node 
        return node 
        

    def remove(self, node: ListNode) -> ListNode:
        if node == self.head or node == self.tail:
            return None  # Cannot remove dummy nodes
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        return node


    def print(self):
        curr = self.head

        while curr:
            print(f"{curr.val}", end = "<-->")
            curr = curr.next
        print()
        


if __name__ == '__main__':
    ll = DoublyLinkedList()
    node10 = ll.insert(10)
    node11 = ll.insert(11)
    node12 = ll.insert(12)
    node118 = ll.insert(118)
    ll.print()
    ll.remove(node10)
    ll.print()
    ll.remove(node118)
    ll.print()
    ll.remove(node11)
    ll.print()
    ll.remove(node12)
    ll.print()