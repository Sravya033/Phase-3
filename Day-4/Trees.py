class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BST:
    def addNode(self,root,value):
        newNode=Node(value)
        if root==None:
            root= newNode
        elif value<root.data:
            if root.left==None:
                root.left=newNode
            else:
                self.addNode(root.left,value)
        elif value>root.data:
            if root.right==None:
                root.right=newNode
            else:
                self.addNode(root.right,value)
        return root
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data,end=" ")
        if root.right!=None:
            self.inorder(root.right)
    def preorder(self,root):
        print(root.data,end=" ")
        if root.left!=None:
            self.preorder(root.left)
        if root.right!=None:
            self.preorder(root.right)    
    def postorder(self,root):
        if root.left!=None:
            self.postorder(root.left)
        if root.right!=None:
            self.postorder(root.right)
        print(root.data,end=" ")
    def levelorder(self,root):
        q=[root]
        while q:
            ele=q.pop(0)
            print(ele.data,end=" ")
            if ele.left!=None:
                q.append(ele.left)
            if ele.right!=None:
                q.append(ele.right)

        
values=[16,9,25,4,10,8,83,15]

tree=BST()
root=None
root=tree.addNode(root,values[0])
for i in range(1,len(values)):
    tree.addNode(root,values[i])
tree.inorder(root)
print()
tree.preorder(root)
print()
tree.postorder(root)
print()
tree.levelorder(root)

