# Implement a data structure SETOFSTACK. It should be composed of several stack and should create a new stack once the previous one exceedds capacity. SETOFSTACK.PUSH() and SETOFSTACK.POP() should behave identically to a single stack that is,pop()should return the same value as it would if there were just a single stack. 



class set_of_stack:
    # Initialization of set_of_classes:
    def __init__(self) -> None:
        self.set_stack=[]
        self.top=[0]*4
        self.current_stack=[]

    # definining push element
    def push(self,element):
        
        if len(self.set_stack)>=3 and self.top[3]==4:
            self.set_stack.append(self.current_stack)
            print("Stack is full   so last element is discarded")
        else:
            if self.top[len(self.set_stack)]!=4:
                self.current_stack.append(element)
                self.top[len(self.set_stack)]+=1

            elif self.top[len(self.set_stack)]==4:
                self.set_stack.append(self.current_stack)
                self.current_stack=[]
                self.current_stack.append(element)
                self.top[len(self.set_stack)]+=1
        
    #defining pop element
    def pop(self):
        if len(self.set_stack)==0 and self.top==[0,0,0,0]:
            print("Stack is Empty")
        else:
            if len(self.set_stack)==4 :
                self.current_stack=self.set_stack.pop()
                self.current_stack.pop()
                self.top[3]-=1
            else:
                self.current_stack.pop()
                self.top[len(self.set_stack)]-=1
    #defining deisplay element
    def display(self):
        print(self.set_stack)
        print(self.current_stack)


# Main Function

if __name__=='__main__':
    stack_op=set_of_stack()
    print("In this program you will perform on set of stack")
    print("There is 4 stack of size 4")

    while(True):
        print("Choose option\n1.Push \n2.Pop \n3.Display\n4.Exit")
        res=int(input())
        if res==1:
            print("Enter element to be pushed")
            ele=int(input())
            stack_op.push(ele)
        elif res==2:
            stack_op.pop()
        elif res==3:
            stack_op.display()
        elif res==4:
            exit(0)
        else:
            print("Wrong Input")
