class ListNode:
    def __init__(self,key,val) -> None:
        self.key=key
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def addll(self,key,val):
        node=ListNode(key,val)
        if self.head==None:
            self.head=self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def find(self,key):
        curr=self.head
        prev=None
        while curr:
            if curr.key==key:
                return prev,curr
            prev=curr
            curr=curr.next
        return None
    
    def get(self,key):
        ele=self.find(key)
        if ele==None:
            return None
        return ele[1]
    
    def delete(self,key):
        ele=self.find(key)
        if ele==None:
            return False
        prev,curr=ele
        if prev==None:
            if self.head==self.tail:
                self.head=self.tail=None
                return
            self.head=self.head.next
        elif curr.next:
            prev.next=curr.next
        else:
            self.tail=prev
            self.tail.next=None
    
    def printll(self):
        curr=self.head
        while curr:
            print("(",curr.key,curr.val,end=' ) -> ')
            curr=curr.next
        print(None)
    
    def give_head(self):
        return self.head
    
    
if __name__ == '__main__':
    linked = LinkedList()
    print(linked.give_head())
    