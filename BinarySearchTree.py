## 이진탐색트리

# 키값은 중복될 수 없다.
# 왼쪽 키값은 루트 키값보다 작다.
# 오른쪽 키값은 루트 키값보다 크다.

# 삽입과정도 일단 탐색과정을 거친다.
# 탐색과정을 거쳐서, 주어진 키값과 일치하는 값을 트리에서 발견할 수 없는 경우, 마지막 위치에 값을 삽입

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_data(self.root, data)

    def _insert_data(self, node, data):
        if node is None:
            node = Node(data)

        else:
            if node.data > data:
                node.right = self._insert_data(node.right, data)
            elif node.data < data:
                node.left = self._insert_data(node.left, data)
            else:
                print('중복된 키값이 존재합니다.')

        return node

    def find(self, data):
        self._find_data(self.root, data)

    def _find_data(self, node, data):
        if node is None:
            print('찾으시는 데이터가 없네요.')
        else:
            if data == node.data:
                print(f'찾으시는 데이터 ${data}를 찾았습니다!')
            elif data > node.data:
                self._find_data(node.right, data)
            else:
                self._find_data(node.left, data)
            
        

def run():
    bst = BinarySearchTree()

    bst.insert(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(35)
    bst.insert(23)

    bst.find(1)

if __name__ == '__main__':
    run()