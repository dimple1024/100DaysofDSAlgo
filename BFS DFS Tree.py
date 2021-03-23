#BFS in tree, Iterative solution
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root=None):
        self.root=root
    def print_bfs_traversal(self,tree,queue=[]):
        node=tree.root
        queue.append(node)
        while queue:
            node=queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return
    def print_dfs_traversal(self,tree,stack=[]):

        node=tree.root
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            print(node.value)
            node=node.right




node=Node(1)
node.left=Node(2)
node.right=Node(3)
node.left.left=Node(4)
node.left.left.left=Node(5)
node.right.left=Node(6)
tree=Tree(node)
tree.print_bfs_traversal(tree,[])
tree.print_dfs_traversal(tree,[])