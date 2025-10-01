from SimpleLinkedList import LinkedList

class PersonalDictionary:

    def __init__(self):
        self.listOfObj=[]

    def __str__(self)->str:
        listOfBuckets=[]

        for i,bucket in enumerate(self.listOfObj):
            listOfNodes=[]
            node=bucket.head
            currentNode=node
            while currentNode!=None:
                listOfNodes.append(f"{currentNode.key} and {currentNode.value}")
                currentNode=currentNode.Next
            listOfBuckets.append(f"Bucket of object {node} with initial key head {node.key}: {listOfNodes}")

        return "\n".join(listOfBuckets)


    def HashFunction(self,valToHash:str)->int:
        hashFunction=0
        for char in valToHash:
            hashFunction+=ord(char)
        return hashFunction
    
    def findIndexOfBucket(self,hashToSearch:int)->bool:
        valuetoSearch=-1
        indextoReturn=-1
        for index,obj in enumerate(self.listOfObj):
            if obj.head is None:
                continue
            hashedObjectSearched=self.HashFunction(obj.head.key)
            if hashedObjectSearched==hashToSearch:
                valuetoSearch=hashedObjectSearched
                indextoReturn=index

        return (True if valuetoSearch!=-1 else False, indextoReturn)



    def updateKeyInDictionary(self,createdLinkedListObject:LinkedList,linkedListObjectToReview:LinkedList)->None:
        newIterableLinkedList=linkedListObjectToReview.head
        if not isinstance(createdLinkedListObject,LinkedList) or not isinstance(linkedListObjectToReview,LinkedList):
            raise TypeError("Object(s) received is not of type Linked list!!")
        else:
            while newIterableLinkedList != None:
                if  newIterableLinkedList.key==createdLinkedListObject.head.key:
                    newIterableLinkedList.value=createdLinkedListObject.head.value
                    return
                newIterableLinkedList=newIterableLinkedList.Next
            #If no return it means it doesnt exist, so add it    
            linkedListObjectToReview.addHead(createdLinkedListObject.head.key,createdLinkedListObject.head.value)


    def addToDictionary(self,key:str,value:int)->None:
        hashedKey=self.HashFunction(key)
        newNodeForDictionary=LinkedList()
        newNodeForDictionary.addHead(key,value)
        doesHashExist,indexOfHash=self.findIndexOfBucket(hashedKey)

        if not doesHashExist: #If -1 means is a new addition
            self.listOfObj.append(newNodeForDictionary) #We add the object reference to the appropiate list
        else: #If exists, handle collition by adding a new linked list item
            objFoundDictionaryNode= self.listOfObj[indexOfHash] #Get the saved key linked list object from that collition
            self.updateKeyInDictionary(newNodeForDictionary,objFoundDictionaryNode)

    def getValue(self,key:str)->list:
        listOfValuesAssociatedWithKey=[]
        hashedKey=self.HashFunction(key)
        doesHashExist,indexOfHash=self.findIndexOfBucket(hashedKey)
        if not doesHashExist:
            raise IndexError("The key" + key +" does not exist in the dictionary!")
        else:
            objFoundDictionaryNode= self.listOfObj[indexOfHash].head #Get the saved key linked list object from that collition
            while objFoundDictionaryNode!=None:
                if objFoundDictionaryNode.key==key:
                    listOfValuesAssociatedWithKey.append(objFoundDictionaryNode.value)
                objFoundDictionaryNode=objFoundDictionaryNode.Next
        return listOfValuesAssociatedWithKey
    
    def removeKey(self,key:str)->None:
        hashedKey=self.HashFunction(key)
        doesHashExist,indexOfHash=self.findIndexOfBucket(hashedKey)

        if not doesHashExist:
            raise IndexError("The key" + key +" does not exist in the dictionary!")
        else:
            indexOfNode=0
            objFoundDictionaryNode= self.listOfObj[indexOfHash].head #Get the saved key linked list object from that collition
            placeHolderNode=None
            while objFoundDictionaryNode!=None:
                if objFoundDictionaryNode.key==key:
                    placeHolderNode=objFoundDictionaryNode.Next
                    self.listOfObj[indexOfHash].deleteAtIndex(indexOfNode)#Delete the nodes associated to that key on the hashmap
                    if self.listOfObj[indexOfHash].head==None:
                        del self.listOfObj[indexOfHash]
                    objFoundDictionaryNode=placeHolderNode
                    continue
                objFoundDictionaryNode=objFoundDictionaryNode.Next
                indexOfNode+=1
    







if __name__=="__main__":
    
    myOwnDictionary=PersonalDictionary()
    myOwnDictionary.addToDictionary("ab",4)
    myOwnDictionary.addToDictionary("ab",5)
    myOwnDictionary.addToDictionary("ab",6)
    #myOwnDictionary.addToDictionary("ab",5)
    myOwnDictionary.addToDictionary("ba",8)
    myOwnDictionary.removeKey("ab")
    print(myOwnDictionary.getValue("ab")
    #myOwnDictionary.addToDictionary("Hola",7)
    #print(myOwnDictionary.getValue("ab"))
    #print(myOwnDictionary.getValue("ba"))
    #print(myOwnDictionary.getValue("Hola"))
    #print(myOwnDictionary)
    #myOwnDictionary.removeKey("sasasas")
    #print(myOwnDictionary.getValue("ab"))
    #print(myOwnDictionary.getValue("ba"))
    pass