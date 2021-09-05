class Node:

    def __init__(self,val) -> None:
        self.value=val
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None


    def insert_node(self,node):
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node


    def traverse_list(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.value)
                temp=temp.next
    def delete_elememt(self,dele_val):
        if self.head==None:
            print("List is empty...Nothing to be deleted")
        else:
            temp=self.head
            if temp.value == dele_val:
                self.head=self.head.next
            else:
                while(temp!=None):
                    if temp.next.value==dele_val:
                        temp.next=temp.next.next
                    
                    temp=temp.next
                    if temp.next==None:
                        break
        




if __name__=='__main__':
    llist=LinkedList()
    num=int(input("How many element you want to enter :"))
    for i in range(num):
        ele=int(input("Enter your element: "))
        temp= Node(ele)
        llist.insert_node(temp)
    print("Here is your list ")
    llist.traverse_list()
    delete_elememt=int(input("Enter your element to be deleted"))
    llist.delete_elememt(delete_elememt)
    print("After deletion of {} from linked list..Here is your list".format(delete_elememt))
    llist.traverse_list()

    
