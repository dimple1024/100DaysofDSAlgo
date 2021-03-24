class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root=None):
        self.root=root
    def right_view_recursive(self,node,level,max_level,output):
        if node == None:
            return
        if level>max_level[0]:
            output.append(node.value)
            max_level[0]=level
        self.right_view_recursive(node.right,level+1,max_level,output)
        self.right_view_recursive(node.left, level + 1, max_level,output)

node=Node(1)
node.left=Node(2)
node.right=Node(3)
node.left.left=Node(4)
node.left.left.left=Node(5)
node.right.left=Node(6)
tree=Tree(node)
output=[]
tree.right_view_recursive(node,1,[0],output)
print(output)




