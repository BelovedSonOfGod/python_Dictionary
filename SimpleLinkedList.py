
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.Next=None



class LinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
    
    def addHead(self,key,value):
        '''
        Insert a node at the head of our linked list
        '''
        if self.head==None:
            self.head=Node(key,value)
            self.tail=self.head
        else:
            newObject=Node(key,value)
            newObject.Next=self.head
            self.head=newObject

    def addTail(self,key,value):
        '''
        Insert a node at the tail of our linked list
        '''
        if self.head==None:
            self.addHead(key,value)
        else:
            newObjectToAdd= Node(key,value)
            self.tail.Next=newObjectToAdd
            self.tail=newObjectToAdd
    
    def get(self,index)->int:
        '''
        Based on a particular index, retrieve the number located at that position on our linked list
        '''
        currentNode=self.head
        indexToSearch=0

        while currentNode!=None:
            if(indexToSearch==index):
                return currentNode.value
            currentNode=currentNode.Next
            indexToSearch+=1

    def addAtIndex(self,index,key,value):
        '''
        Inserts a node at the given index (shifts existing elements to the right).
        '''
        currentNode=self.head
        previouscurrentNode=None
        indexToSearch=0

        if index<0:
            raise IndexError("Index out of range")
        
        if index==0:
            self.addHead(value)
            return
        
        while  currentNode!=None :
            if indexToSearch==index:
                objectToAdd= Node (key,value)
                previouscurrentNode.Next=objectToAdd
                objectToAdd.Next=currentNode
                return
            previouscurrentNode=currentNode
            currentNode=currentNode.Next
            indexToSearch+=1


        

        self.addTail(value)
        

        

        currentNode=self.head
        indexToSearch=0

    def deleteAtIndex(self,index):
        '''
        Deletes the node of the desired index
        '''
        currentNode=self.head
        previouscurrentNode=None
        indexToSearch=0

        if index<0:
            raise IndexError("Index out of range")
        
        if index==0:
            previouscurrentNode=self.head
            self.head=currentNode.Next
            del previouscurrentNode
            return
        
        while  currentNode!=None :
            if indexToSearch==index:
                    previouscurrentNode.Next=currentNode.Next
                    if currentNode==self.tail:
                        self.tail=previouscurrentNode
                    del previouscurrentNode
                    return

                    
            previouscurrentNode=currentNode
            currentNode=currentNode.Next
            indexToSearch+=1



    def printLinkedList(self):
        '''
        Prints the linkedlist starting from the head, all in a single line thanks to end="" which makes avoiding printing a new line inmediatly, and at the end it printos a linebreak for future prints
        '''
        currentNode=self.head

        while currentNode!=None:
            print(str(currentNode.keyValuePair) + "(" + str(id(currentNode)) + ")" + "->" ,end="")
            currentNode=currentNode.Next
        print()


if __name__=="__main__":
    MynewLinkedList= LinkedList()

    MynewLinkedList.addHead("h",0)
    MynewLinkedList.printLinkedList()
    MynewLinkedList.addHead("o",-1)
    MynewLinkedList.printLinkedList()
    MynewLinkedList.addTail("l",6)
    MynewLinkedList.addTail("a",7)
    MynewLinkedList.printLinkedList()
    MynewLinkedList.addAtIndex(2,"l",6.5)
    MynewLinkedList.printLinkedList()
    MynewLinkedList.deleteAtIndex(0)
    MynewLinkedList.printLinkedList()
    MynewLinkedList.deleteAtIndex(3)
    MynewLinkedList.printLinkedList()
    MynewLinkedList.deleteAtIndex(100)        
    MynewLinkedList.printLinkedList()