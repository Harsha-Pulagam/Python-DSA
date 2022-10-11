# Run in your local for more clarity of the program
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
  '''
  For this the following output will be like...
  --Prorder--

            Root                            --Root
            LeftChild
            L - LeftChild                   # L - Leftchild -> Leftside of Leftchild to root
            L - RightChild                  # L - Leftchild -> Leftside of Rightchild to root
            RightChild
            R - Leftchild                   # R - Rightchild -> Leftside of Rightchild to root
            R - RightChild
  '''

def inOrder(root): #left-> root ->right
  if not root:
    return
  preOrder(root.left)
  print(root.data)
  preOrder(root.right)
  '''
  --Inorder--

          LeftChild 
          L - LeftChild
          L - RightChild
          Root                              --Root
          RightChild
          R - Leftchild
          R - RightChild  
  '''

def postOrder(root): #left -> right -> root
  if not root:
    return
  preOrder(root.left)
  preOrder(root.right)
  print(root.data)
  
  '''
  --Postorder--

          LeftChild
          L - LeftChild
          L - RightChild
          RightChild
          R - Leftchild
          R - RightChild
          Root                                --Root
  '''
  
  
  
  

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
