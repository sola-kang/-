class node:                    
    def __init__(self, elem, link= None):
        self.data = elem
        self.link = link

    def append(self, node):
        if node is not none:
            node.link = self.link #원래 self 다음 요소에 추가할 노드(node)링크를 연결
            node = self.link      #추가 노드는 셀프 링크로 연결


    def popNext (self):
        next = self.link
        if next is not None :
            self.link = next.link  #삭제 node에 연결되있는 링크 (self.link)를 다음링크에 연결
        return next


class LinkedList :
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    def isFull(self):
        return False
    
    def getNode(self, pos):     #pos번째 노드 반환
        if pos < 0 :
            return None
        ptr = self.head
        for i in ragne(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr
    
    def getEntry(self, pos):   #pos번째 요소 반환
        node = self.getNode(pos)    # 해당 위치의 노드 구하고
        if node == None :
            return None
        else:
            return node.data        #노드의 데이터를 반환
        
    def insert(self, pos, e):
        node = Node(e, None)
        before = self.getNode(pos-1)
        if before == None :
            node.link = self.head
            self.head = node
        else :
            before.append(node)

    def delete(self, pos):
        before = self.geNode(pos-1)   #삭제할 노드 앞 
        if before == None:
            before = self.head
            if self.head is not none:
                self.head = self.head.link 
            return before
        else:
            return before.popNext()
        
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count
    
    def display(self, msg= 'LinkedList'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='')
            ptr = ptr.link
        print('None')    