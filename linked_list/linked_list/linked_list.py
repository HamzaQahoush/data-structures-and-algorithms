class Node :
    def __init__(self,value):
        self.value=value
        self.next = None


class Linked_List:
    def __init__(self,):
        self.head = None   
        self.length=0          # initiate the value head= None
        
    def insert(self,value):           # inesert at begining of linked list
        new_node = Node(value)
        if not self.head:
            self.head=new_node
        else :
            new_node.next=self.head 
            self.head=new_node   


    def append (self,value): #define append method add to end of linked list
        new_node = Node(value)     #setup the new_node to Node(value)
        if self.head:             #check self.head if contains a value 
            current= self.head    # set our current value to head 
            while current.next:    # while current.next != None , set current = current.next and move
                current=current.next
            current.next  =new_node   # assign new node to current.next
        else: 
            self.head=new_node         # in case self.head = None set it to new_node 

    def include (self,value):
        if not self.head:
            return False
        else:
            current_node=self.head
            while current_node != None:
                if current_node.value == value:
                    return True 
                else:
                    current_node=current_node.next
            return False


    def __str__(self):
        # return a string shows linked list { a } -> { b } -> { c } -> NULL"   
        current= self.head
        result=""
        while current:
            result+=f"{ current.value } -> "
            current=current.next
        result+= "Null"  
        return result      
        
    def printList(self):
	    temp = self.head
	    while (temp):
		    print (temp.value,)
		    temp = temp.next

    def insertAfter(self ,value, newVal) :
        node=Node(newVal)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                
                if current.value==value:
                    bef_val=current.next
                    current.next =node
                    
                    node.next=bef_val
                    self.length+=1
                    return node.value
                current=current.next




    def insertBefore(self,value, newVal):
        new_node = Node(newVal)
        current = self.head
        if current.value == value:
            new_node.next = current
            self.head = new_node
        else:
            while current.next:

                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    self.length+=1
                    break
                current = current.next




# if __name__ == "__main__":
#  ll=Linked_List()
#  ll.insert("Hamza")
#  ll.insert("Akram")
#  ll.append(4)
#  ll.append('ahmad')
# #  ll.append('s')
# #  print(ll.head.value)
# #  print(ll.head.next.value)
# #  print(ll.head.next.next.value)
#  print(ll.__str__())
# #  print (ll.include('Hamza'))
# #  print (ll.include('akram'))
#  print(ll.printList())