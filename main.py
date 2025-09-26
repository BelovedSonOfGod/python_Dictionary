from SimpleLinkedList import LinkedList

class PersonalDictionary:

    def __init__(self):
        self.listOfObj=[]

    def HashFunction(self,valToHash:str)->int:
        hashFunction=0
        for char in valToHash:
            hashFunction+=ord(char)
        return hashFunction
    
    def findIndexOfBucket(self,hashToSearch:int)->bool:
        valuetoSearch=-1
        indextoReturn=-1
        for index,obj in enumerate(self.listOfObj):
            hashedObjectSearched=self.HashFunction(obj.head.key)
            if hashedObjectSearched==hashToSearch:
                valuetoSearch=hashedObjectSearched
                indextoReturn=index

        return (True if valuetoSearch!=-1 else False, indextoReturn)



    def addToDictionary(self,key:str,value:int)->None:
        hashedKey=self.HashFunction(key)
        newNodeForDictionary=LinkedList()
        newNodeForDictionary.addHead(key,value)
        doesHashExist,indexOfHash=self.findIndexOfBucket(hashedKey)

        if not doesHashExist: #If -1 means is a new addition
            self.listOfObj.append(newNodeForDictionary) #We add the object reference to the appropiate list
        else: #If exists, handle collition by adding a new linked list item
            objFoundDictionaryNode= self.listOfObj[indexOfHash] #Get the saved key linked list object from that collition
            objFoundDictionaryNode.addTail(key,value)

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
                    objFoundDictionaryNode=placeHolderNode
                    continue
                objFoundDictionaryNode=objFoundDictionaryNode.Next
                indexOfNode+=1
    







if __name__=="__main__":
    myOwnDictionary=PersonalDictionary()
    myOwnDictionary.addToDictionary("ab",4)
    myOwnDictionary.addToDictionary("ab",5)
    myOwnDictionary.addToDictionary("ba",8)
    myOwnDictionary.addToDictionary("Hola",7)
    print(myOwnDictionary.getValue("ab"))
    print(myOwnDictionary.getValue("ba"))
    print(myOwnDictionary.getValue("Hola"))
    myOwnDictionary.removeKey("ab")
    print(myOwnDictionary.getValue("ab"))
    print(myOwnDictionary.getValue("ba"))
    pass



'''
What to do next:
Muy bien 👌, te voy guiando como tu tech lead:

✅ Lo que ya lograste

Tienes una clase PersonalDictionary.

Implementaste una hash function simple (suma de ord(char)), suficiente para empezar.

Guardas pares hash → LinkedList de valores en dos listas paralelas (listOfObjPosition y listOfHashObj).

Ya puedes añadir un valor nuevo para una clave y manejar colisiones (con una linked list).

Eso es justo el paso 1 que tocaba: guardar cosas en buckets. Vas bien 🚀.

🔍 Observaciones / Siguientes mejoras

Separación de responsabilidades

Ahorita usas listOfHashObj y listOfObjPosition en paralelo.

Una forma más limpia sería tener una sola lista de “buckets”, donde cada bucket contiene (hash, LinkedList). Así reduces riesgo de desincronización.

Pero para practicar, está bien que uses dos listas por ahora.

LinkedList

Cuando haces:

objFoundDictionaryNode.next = newNodeForDictionary


eso reemplaza el next, no lo agrega al final. En otras palabras, si ya había varios nodos, los pierdes.
👉 Lo correcto sería recorrer la linked list hasta el final y luego enlazar ahí.

Clave vs Hash

Estás guardando el hash pero no la clave original.

Si dos claves distintas producen el mismo hash (colisión), no podrías distinguirlas.

Lo ideal es que en la linked list cada nodo guarde un (key, value), no solo value.

📌 Checklist de avance (para ti, no lo resuelvo, solo guío):


 ~~Ajustar addToDictionary para que en colisiones recorras la lista y agregues al final.~~

 ~~Implementar getValue(key) que busque dentro de la linked list del bucket correcto.~~

 ~~(Opcional, para practicar más) Implementar remove(key)~~.

 📌Checklist de lo que falta (mañana puedes avanzar):

 Cambiar nodos de tu LinkedList para guardar (key, value) en lugar de solo value.

 Ajustar addToDictionary para insertar (key, value) en cada nodo.

 Ajustar getValue para filtrar por clave → devolver solo valores que tengan el mismo key.

 Ajustar removeKey para eliminar nodos con la clave exacta, no solo el bucket entero.

 probar y documentar.
'''