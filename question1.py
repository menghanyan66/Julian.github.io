import collections

def postorderTraversal(preorder, inorder):
    if not preorder or not inorder:
        return ''
    
    root = preorder[0]
    mid = inorder.index(root)
    left_inorder = inorder[:mid]
    right_inorder = inorder[mid+1:]
    
    left_preorder = preorder[1:mid+1]
    right_preorder = preorder[mid+1:]
    
    left_postorder = postorderTraversal(left_preorder, left_inorder) 
    right_postorder = postorderTraversal(right_preorder, right_inorder)

    return left_postorder + right_postorder + root

preorder = input().strip() 
inorder = input().strip()

print(postorderTraversal(preorder, inorder))
