'''给定一个二叉树，计算 整个树 的坡度 。
一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树
节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；
没有右子树的话也是一样。空结点的坡度是 0 。
整个树 的坡度就是其所有节点的坡度之和。
TreeNode.left 节点左子节点
TreeNode.right 节点右子节点
TreeNode.val 节点值

'''


class solution:
    def __init__(self):
        self.result = 0

    '''
        TreeNode:二叉树节点
    '''

    def findTilt(self, TreeNode):
        self.dfs(TreeNode)
        return self.result

    def dfs(self, node):
        if not node:
            return 0
        #递归获取根节点的左叶子节点的总坡度
        sum_left = self.dfs(node.left)
        # 递归获取根节点的右叶子节点的总坡度
        sum_right = self.dfs(node.right)
        #获取
        #abs返回函数绝对值
        self.result += abs(sum_right - sum_left)
        return sum_left + sum_right + node.val
