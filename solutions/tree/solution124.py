# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        if root.left is None and root.right is None:
            return root.val
        elif root.left is None and root.right is not None:
            open_right_val = self.maxOpenSum(root.right)
            close_right_val = self.maxPathSum(root.right)
            val = max(open_right_val + root.val, open_right_val, open_right_val, root.val, close_right_val)

        elif root.left is not None and root.right is None:
            open_left_val = self.maxOpenSum(root.left)
            close_right_val = self.maxPathSum(root.left)

            val = max(open_left_val + root.val, open_left_val, open_left_val, root.val, close_right_val)
        else:
            open_left_val = self.maxOpenSum(root.left)
            open_right_val = self.maxOpenSum(root.right)
            close_right_val = self.maxPathSum(root.left)
            close_left_val = self.maxPathSum(root.right)

            val = max(root.val, open_right_val, open_left_val, close_right_val, close_left_val,
                      root.val + open_right_val, root.val + open_left_val,
                      open_left_val + root.val + open_right_val)
        # print("当前节点:{},最长路径:{}".format(root.val, val))

        return val

    def maxOpenSum(self, root: TreeNode) -> int:
        # 找出以当前节点为一端的最长路径
        if root.left is None and root.right is None:
            val = root.val
        elif root.left is None and root.right is not None:
            val = max(root.val + self.maxOpenSum(root.right), root.val)
        elif root.left is not None and root.right is None:
            val = max(root.val + self.maxOpenSum(root.left), root.val)
        else:
            val = max(root.val + self.maxOpenSum(root.left),
                      root.val + self.maxOpenSum(root.right),
                      root.val)
        # print("当前节点:{},最长开放路径:{}".format(root.val, val))

        return val


if __name__ == '__main__':
    # node1 = TreeNode(1)
    # node2 = TreeNode(-2)
    # node3 = TreeNode(-3)
    # node4 = TreeNode(1)
    # node5 = TreeNode(3)
    # node6 = TreeNode(-2)
    # node7 = TreeNode(-1)
    #
    # node1.left = node2
    # node1.right = node3
    #
    # node2.left = node4
    # node2.right = node5
    # node3.left = node6
    #
    # node4.left = node7
    node6 = TreeNode(-1)
    node7 = TreeNode(5)
    node8 = TreeNode(4)
    node9 = TreeNode(2)
    node10 = TreeNode(-4)
    node6.left = node7
    node7.left = node8
    node8.right = node9
    node9.left = node10

    solution = Solution()

    max_open = solution.maxPathSum(node6)
    print(max_open)
