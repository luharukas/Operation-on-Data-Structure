# Python3 program to detect loopin the linked list
# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next

	def detectLoop(self):
		s = set()
		temp = self.head
		while (temp):
			if (temp in s):
				return True
			# the first time, insert it in hash
			s.add(temp)

			temp = temp.next

		return False


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop ")

