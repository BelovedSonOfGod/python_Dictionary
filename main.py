from SimpleLinkedList import LinkedList

class PersonalDictionary:

    def __init__(self):
        self.listOfObjPosition=[]
        self.listOfHashObj=[]

    def HashFunction(self,valToHash:str)->int:
        hashFunction=0
        for char in valToHash:
            hashFunction+=ord(char)
        return hashFunction
    
    def searchForHash(self,hashToSearch:int)->bool:
        valuetoSearch=-1
        indextoReturn=-1
        for index,objHash in enumerate(self.listOfHashObj):
            if objHash==hashToSearch:
                valuetoSearch=objHash
                indextoReturn=index

        return (True if valuetoSearch!=-1 else False, indextoReturn)



    def addToDictionary(self,key:str,value:int)->None:
        hashedKey=self.HashFunction(key)
        newNodeForDictionary=LinkedList()
        newNodeForDictionary.addHead(value)
        doesHashExist,indexOfHash=self.searchForHash(hashedKey)

        if not doesHashExist: #If -1 means is a new addition
            self.listOfObjPosition.append(newNodeForDictionary) #We add the object reference to the appropiate list
            self.listOfHashObj.append(hashedKey) # we save the hash to same position as the other list
        else: #If exists, handle collition by adding a new linked list item
            objFoundDictionaryNode= self.listOfObjPosition[indexOfHash] #Get the saved key linked list object from that collition
            objFoundDictionaryNode.addTail(newNodeForDictionary)

    def getValue(self,key:str)->list:
        listOfValuesAssociatedWithKey=[]
        hashedKey=self.HashFunction(key)
        doesHashExist,indexOfHash=self.searchForHash(hashedKey)
        if not doesHashExist:
            raise IndexError("The key" + key +" does not exist in the dictionary!")
        else:
            objFoundDictionaryNode= self.listOfObjPosition[indexOfHash] #Get the saved key linked list object from that collition
            while objFoundDictionaryNode!=None:
                listOfValuesAssociatedWithKey.append(objFoundDictionaryNode.value)
                objFoundDictionaryNode=objFoundDictionaryNode.next
        return listOfValuesAssociatedWithKey
    
    def removeKey(self,key:str)->None:
        hashedKey=self.HashFunction(key)
        doesHashExist,indexOfHash=self.searchForHash(hashedKey)

        if not doesHashExist:
            raise IndexError("The key" + key +" does not exist in the dictionary!")
        else:
            self.listOfObjPosition.remove(indexOfHash)
            self.listOfHashObj.remove(hashedKey)
    







if __name__=="__main__":
    myOwnDictionary=PersonalDictionary()
    myOwnDictionary.addToDictionary("Hola",4)
    myOwnDictionary.addToDictionary("Hola",5)
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

Próximos métodos
Ahora mismo solo tienes addToDictionary. Lo siguiente sería:

getValue(key) → devolver el valor (o lista de valores) asociado a la clave.

remove(key) → eliminar la clave.

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