from solutions.utils.tree import TreeNode


class Solution:
    # 后序遍历
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        right = self.invertTree(root.left)
        left = self.invertTree(root.right)
        root.right = right
        root.left = left
        return root

    # 前序遍历
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        temp = root.right
        root.right = self.invertTree(root.left)
        root.left =self.invertTree(temp)


        return root


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3, node1, node2)
    node4 = TreeNode(4)
    node5 = TreeNode(5, node3, node4)

    solution = Solution()
    res = solution.invertTree1(node5)
    print(res)
