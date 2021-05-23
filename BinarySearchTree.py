## 이진탐색트리

# 키값은 중복될 수 없다.
# 왼쪽 키값은 루트 키값보다 작다.
# 오른쪽 키값은 루트 키값보다 크다.

# 삽입과정도 일단 탐색과정을 거친다.
# 탐색과정을 거쳐서, 주어진 키값과 일치하는 값을 트리에서 발견할 수 없는 경우, 마지막 위치에 값을 삽입

import copy

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def search(self, x):
        p = self.root

        while p != None:
            if p.data == x:
                print(f'값 {x} (을/를) 찾았습니다.')
                return 0

            else:
                if p.data < x:
                    p = p.left
                else:
                    p = p.right

        print('값이 없습니다.')

    def insert(self, x):
        p = None
        t = self.root

        while t != None:
            if t.data == x: return
            p = t
            if p.data < x: t = p.left
            else: t = p.right
        
        n = Node(x)
        if p is not None:
            if p.data < x: p.left = n
            else: p.right = n
        
        else:
            self.root = n

    def delete(self, x):
        p = None 
        t = self.root

        while t is not None and t.data != x:
            p = t
            t = p.left if p.data < x else p.right
        
        if t == None:
            print('값이 없습니다.')
            return
        
        if t.left is None and t.right is None:
            if p is not None:
                if p.left == t:
                    p.left = None
                
                else:
                    p.right = None
            
            else:
                self.root = None

        elif t.left is None or t.right is None:
            child = t.left if t.left is not None else t.right
            if p is not None:
                if p.left == t:
                    p.left = child
                else:
                    p.right = child

            else:
                self.root = None

        else:
            succ_p = t
            succ = t.right

            while succ.left is not None:
                succ_p = succ
                succ = succ.left

            if succ_p.left == succ:
                succ_p.left = succ.right
            else:
                succ_p.right = succ.right
            
            succ.left = t.left
            succ.right = t.right
            
        del t
        print(f'값 {x} (이/가) 삭제되었습니다.')

def run():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.insert(6)

    bst.search(3)

    bst.delete(7)


if __name__ == '__main__':
    run()