class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self) -> None:
        self.head=None
        self.part=None
    
    def push_from_back(self,node):
        self.part.next=node
        self.part=self.part.next




    def push_from_front(self,node):
        if self.head==None:
            self.head=node
            self.part=node
            print("head")
        else:
            node.next=self.head
            self.head=node
            print("node")


    def traverse(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data)
                temp=temp.next



if __name__=='__main__':
    llist=linked_list()

    partition_ele=int(input("Enter partioned element"))
    node=Node(partition_ele)
    llist.push_from_front(node)

    num=int(input("How many element you want to enter"))
    for i in range(num):
        ele=int(input("Enter your element"))
        node=Node(ele)
        if ele>=partition_ele:
            llist.push_from_back(node)
        else:
            llist.push_from_front(node)

    
    print("After partioning list look like ")
    llist.traverse()
        
    

