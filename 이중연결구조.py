class DNode:   #이중 연결 구조를 위한 정의와 생성자 
    def __init__(self, elem, prev=None, next=None):  #아직 아무것도 연결x상태 -> 명시적으로 표현
        self.data = elem 
        self.prev = prev
        self.next = next

    def append(self, node):                #추가 연산
        if node is not None:              #리스트가 공백이 아니면
            node.next = self.next         #추가하려는 노드 다음링크를 원래노드(self)다음노드 가리키게함
            node.prev = self              #추가 노드 이전 노드는 현재 self노드로 연결
            if node.next is not None :    #만약 추가 노드 다음이 안비어있으면
                node.next.prev = node     #추가노드 다음 이전링크를 추가노드(node)에 연결
            self.next = node              #즉 현재 self.다음 노드는 추가노드로 설정됨

    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next         #삭제하려는 노드의 다음링크가 self노드의 다음링크가 됨 만약 다음노드 없으면 self.next가 none으로설정
            if self.next is not None:
                self.next.prev = self
        return node                       #삭제한 노드 반환
        
class DbLinkedList:
    def __init__(self):
        self.head = None

    def display(self, msg="DbLinkedList:" ):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>')
            ptr = ptr.next               #이중연결리스트에는 prev가 있기때문에 다음링크는 next로 표현한다
        print('None')
    
    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos-1)
        if before ==None :
            node.next = self.head       #머리노드에 삽입하는 경우 현재 새로운 node 다음링크가 현재 head가리킴
            if node.next is not None:
                node.next.prev = node   #다음노드의 이전링크가 새 노드를 가리킴
            self.head = node            #새 노드가 head가 된다
        else:
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head          #before을 현재 head(삭제예정)로 만듬
            if self.head is not None :  
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None   #head는 이전링크가 없기때문에 None
            return before               #before 삭제
        else:
            before.popNext()

s = DbLinkedList()

s.display('연결리스트(초기):')
s.insert(0,10)