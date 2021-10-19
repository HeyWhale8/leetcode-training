from solutions.utils.tree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:



        def compare(node1, node2):
            if node1 is None and node2 is None:
                return True
            if not node1 or not node2:
                return False


            return node1.val == node2.val and compare(node1.left, node2.right) and compare(node1.right, node2.left)

        return compare(root, root)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3, node1, node2)
    node4 = TreeNode(4)
    node5 = TreeNode(5, node3, node4)

    solution = Solution()
    res = solution.isSymmetric(node5)
    print(res)
