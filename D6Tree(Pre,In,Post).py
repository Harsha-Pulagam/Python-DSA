class TreeNode:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

def preOrder(root): #root ->left ->right
  if not root:
    return
  print(root.data)
  preOrder(root.left)
  preOrder(root.right)

def inOrder(root): #left-> root ->right
  if not root:
    return
  preOrder(root.left)
  print(root.data)
  preOrder(root.right)

def postOrder(root): #left -> right -> root
  if not root:
    return
  preOrder(root.left)
  preOrder(root.right)
  print(root.data)

rootNode = TreeNode("Root")

lc = TreeNode("LeftChild")
llc = TreeNode("L - LeftChild")
lrc = TreeNode("L - RightChild")

rc = TreeNode("RightChild")
rlc = TreeNode("R - Leftchild")
rrc = TreeNode("R - RightChild")

rootNode.left=lc
rootNode.right=rc

lc.left  = llc
lc.right = lrc

rc.left  = rlc
rc.right = rrc

print("--Prorder--")
print()
preOrder(rootNode)
print()
print("--Inorder--")
print()
inOrder(rootNode)
print()
print("--Postorder--")
print()
postOrder(rootNode)
