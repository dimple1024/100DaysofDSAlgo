class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root=None):
        self.root=root
    #Iterative solution
    def rightView(self,root):
        queue=[]
        data_q=[]
        queue.append(root)
        while queue:
            length=len(queue)
            while length:
                node=queue.pop(0)
                data_q.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length-=1
            data_q.append("S")
        output=[]
        for i in range(len(data_q)-1):
            if data_q[i+1]=="S":
                output.append(data_q[i])
        print(output)

node=Node(1)
node.left=Node(2)
node.right=Node(3)
node.left.left=Node(4)
node.left.left.left=Node(5)
node.right.left=Node(6)
tree=Tree(node)

tree.rightView(node)
