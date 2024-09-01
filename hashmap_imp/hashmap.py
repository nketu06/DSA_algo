from linkedlist import LinkedList
import hashlib

class hashmap:
    def __init__(self) -> None:
        self.size=0
        self.arr=[LinkedList()]*2
        self.capacity=len(self.arr)

    def __hash(self,key)->int:
        key_str = str(key)
        return int(hashlib.sha256(key_str.encode()).hexdigest(), 16)
    
    # return linkedlist object for the given key
    def __find_bucket_ll(self,key,arr)->LinkedList:
        bucket=self.__hash(key)%self.capacity
        return arr[bucket]
    
    # it will insert or update val for key
    def __insert(self,key,value,arr)->None:
        linkedlist=self.__find_bucket_ll(key,arr)
        node=linkedlist.get(key)
        if node==None:
            linkedlist.addll(key,value)
            self.size+=1
        else:
            node.val=value

    # create new array
    def __rehash(self)->None:
        self.capacity=self.capacity*2
        newarr=[LinkedList()]*(self.capacity)
        for linkedlist in self.arr:
            head=linkedlist.give_head()
            while head:
                self.__insert(head.key,head.val,newarr)
                head=head.next
        self.arr=newarr

    # add key,val in the map, also rehash if required
    def put(self,key,value)->None:
        load_factor = self.size/self.capacity
        if load_factor>=2:
            self.size=0
            self.__rehash()
        self.__insert(key,value,self.arr)

    # return value for the key
    def get(self,key) -> int:
        bucket=self.__hash(key)%self.capacity
        linkedlist=self.arr[bucket]
        node=linkedlist.get(key)
        if node:
            return node.val
        return None
    
    # remove element from hashmap
    def remove(self,key)->None:
        bucket=self.__hash(key)%self.capacity
        linkedlist=self.arr[bucket]
        linkedlist.delete(key)
        self.size-=1


# ---------------------->>>> TESTING <<<<---------------------------
if __name__ == '__main__':
    hm1=hashmap()
    hm1.put("a",1)
    print(hm1.size,'size','|',hm1.capacity,"capacity")
    hm1.put("b",2)
    hm1.put("c",3)
    hm1.put("d",4)
    print(hm1.size,'size','|',hm1.capacity,"capacity")
    hm1.put("e",5)
    hm1.put('f',6)
    hm1.put('g',7)
    hm1.put("h",8)
    print(hm1.size,'size','|',hm1.capacity,"capacity")
    print(hm1.get('a'))
    hm1.put("a",100)
    print(hm1.get('a'))
    hm1.put("a",10099)
    print(hm1.get('a'))
    hm1.remove('a')
    print(hm1.get('a'))

    hm1.remove("b")
    hm1.remove("c")
    hm1.remove("d")
    print(hm1.size,'size','|',hm1.capacity,"capacity")
    hm1.remove("e")
    hm1.remove('f')
    hm1.remove('g')
    hm1.remove("h")
    print(hm1.size,'size','|',hm1.capacity,"capacity")
