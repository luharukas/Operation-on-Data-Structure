# An animal shelter, which holds only dog and cats, operates on a strictly FIFO. basis. People must adopt either the oldest(based on arrival time) of all animal at the shelter.They cannot select which specific animal they would like. Create the data structure to maintain this system and implement operation such as enqueue, dequeuANy, dequeueDog, and dequeueCat. 
#you may use linked list datastructure.
class animal:
    def __init__(self,name,typ) -> None:
        self.name=name
        self.typ=typ
        self.next=None




class animal_shelter:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def enqueue(self,node):
        if self.head==None :
            print("head and tail set")
            self.head=node
            self.tail=node

        else:
            print("Moved forward")
            self.tail.next=node
            self.tail=self.tail.next



    def dequeueany(self):
        temp=self.head
        self.head=self.head.next
        print("Congrats you adopted {}".format(temp.name))
        del(temp)

    def dequeuedog(self):
        if self.head==None:
            print("Shelter is empty")
        elif self.head.typ=='D':
            animal_shelter.dequeueany(self)
        else:
            temp=self.head
            while(temp.next!=None):
                if temp.next.typ=='D':
                    temp2=temp.next
                    temp.next=temp.next.next
                    print("Congrats you adopted {}".format(temp2.name))
                    del(temp2)
                    break
                temp=temp.next


    def dequeuecat(self):
        if self.head==None:
            print("Shelter is empty")
        elif self.head.typ=='C':
            animal_shelter.dequeueany(self)
        else:
            temp=self.head
            while(temp.next!=None):
                if temp.next.typ=='C':
                    temp2=temp.next
                    temp.next=temp.next.next
                    print("Congrats you adopted {}".format(temp2.name))
                    del(temp2)
                    break
                temp=temp.next


    def display(self):
        temp=self.head
        if temp==None:
            print("Shelter is empty")
        else:
            while temp!=None:
                print("Name: {}\nType: {}".format(temp.name,temp.typ))
                temp=temp.next

        









if __name__=='__main__':
    ani_she=animal_shelter()
    while(True):
        print("What would you like to do\n1.Input animal\n2.Adopt Dog\n3. Adopt Cat\n4. Adopt Any\n5. Display dataset\n6.Exit")
        res=int(input())
        if res==1:
            print("Enter name of pet")
            name=input()
            typ=input("Enter type D for Dog and C for Cat")
            node=animal(name,typ)
            ani_she.enqueue(node)

        elif res==2:
            ani_she.dequeuedog()

        elif res==3:
            ani_she.dequeuecat()

        elif res==4:
            ani_she.dequeueany()
        elif res==5:
            ani_she.display()
        elif res==6:
            exit(0)

        else:
            print("Wrong Input")








