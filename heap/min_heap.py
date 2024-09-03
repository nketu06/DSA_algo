class MinHeap:
    def __init__(self) -> None:
        self.arr=[5,12,20,25,13,24,22,35,34]
        self.size=len(self.arr)

    
    def __upheapify(self):
        idx=self.size-1
        while idx>0:
            parent=(idx-1)//2
            if self.arr[idx]<self.arr[parent]:
                self.arr[idx],self.arr[parent]=self.arr[parent],self.arr[idx]
            else:
                break
            idx=parent

    def insert(self,num) -> None:
        self.arr.append(num)
        self.size+=1
        self.__upheapify()


    def __downheapify(self):
        idx=0
        while ((idx*2)+1) < self.size:
            lc,rc=(idx*2)+1,(idx*2)+2
            minimum=min(self.arr[idx],self.arr[lc])
            if rc:
                minimum=min(minimum,self.arr[rc])

            if minimum==self.arr[idx]:
                break
            elif minimum == self.arr[lc]:
                self.arr[lc],self.arr[idx]=self.arr[idx],self.arr[lc]
                idx=lc
            else:
                self.arr[rc],self.arr[idx]=self.arr[idx],self.arr[rc]
                idx=rc


    def remove(self) -> int:
        ans=self.arr[0]
        last_idx=self.size-1
        self.arr[0],self.arr[last_idx]=self.arr[last_idx],self.arr[0]
        self.arr.pop()
        self.size-=1
        self.__downheapify()
        return ans




if __name__ == '__main__':
    mh=MinHeap()
    print(mh.arr)
    mh.insert(10)
    print("added 10 \n",mh.arr)
    mh.remove()
    print("removed min\n",mh.arr)


    
