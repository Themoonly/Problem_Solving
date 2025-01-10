# การเขียนโปรแกรม class
# โปรแกรมนี้ มี 2 class

# Node class
    # มีฟังชั่นเดี่ยวคือ Constructor คือตอนที่สร้างออฟเจค จะวิ่งมาที่ init โดยอัตโนมัต 
class Node:
    # 1 def
    # Constructor to initialize the node object
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList:
    # 4 def
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):
        print("Delete node "+(str)(key))
        temp = self.head
        while temp:
            if temp.data == key:
                temp.data = None
                break
            x = temp
            temp = temp.next
        x.next = temp.next

    # def deleteNode(self, key):
    #     print("Delete node "+(str)(key))
    #     temp = self.head
    #     while temp:
    #         if temp.data == key:
    #             temp.data = None
    #             break
    #         x = temp
    #         temp = temp.next
    #     x.next = temp.next
    #     print(temp.data)

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next

if __name__ == "__main__": 
    llist = LinkedList()
    llist.push(7) # ส่งเลข 7 ไปให้ new data
    llist.push(1) 
    llist.push(3)
    llist.push(2)
    print ("Created Linked List: ")
    llist.printList()
    llist.deleteNode(1)
    print ("Linked List after Deletion of 1:")
    llist.printList()