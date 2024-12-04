def DFS(root, target):
    """
    Return True if there is a path from root to target using DFS.
    """
    visited = set()
    stack = []

    visited.add(root)
    stack.append(root)

    while stack:
        cur = stack.pop()  # Get the top element of the stack
        if cur == target:
            return True
        
        # Iterate through neighbors of the current node
        for neighbor in cur.neighbors:  # Assuming 'cur' has a 'neighbors' attribute
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.dfs(root,result)

    
    def dfs(self,root,result):
        if root is None:
            return

        self.dfs(root.left,result)
        result.append(root.val,result)        
        self.dfs(root.right,result)
        
        return result
    
class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        num = 0
        letter = ''
        self.dfs(s,0,result,num,letter)
        result = ''.join(result)
        return result

    def dfs(self,s,i,result,num,letter):

        if i == len(s):
            return
        
        if s[i] in '1234567890':
            num = s[i]
        elif s[i] == '[':
            letter = ''
            self.dfs(s,i+1,result,num,letter)
        elif s[i] == ']':
            result.append(num*letter)
        else:
            letter += s[i]
            self.dfs(s,i+1,result,num,letter)


