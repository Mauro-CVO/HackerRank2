class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                #print('rl:', cur)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
                #print('rr:', root.right)
        return root

    def getHeight(self,root):
        if not root:
            return -1
        if not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        print('left_height:', left_height)
        right_height = self.getHeight(root.right)
        print('right_height:', left_height)
        print('max:', max(left_height,right_height))
        return max(left_height, right_height) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
    print('-------------------------------------------------------------------------')
    print('data:', data)
height=myTree.getHeight(root)
print(height)       