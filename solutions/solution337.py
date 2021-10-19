from utils import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, status):
            '''
            :param root: 当前节点
            :param status: 是否可偷
            :return:
            '''
            if root is None:
                return 0

            hop = dfs(root.left, True) + dfs(root.right, True)
            rob =  dfs(root.left, False) + dfs(root.right, False)
            if status:
                gain = max(root.val + rob,hop)
            else:
                gain = hop
            return gain

        def dfs1(root: TreeNode) -> (int, int):
            '''
            :param root: 当前节点
            :return:(rob,hop)
            '''
            if root is None:
                return 0, 0
            left = dfs1(root.left)
            right = dfs1(root.right)
            rob = root.val + left[1] + right[1]
            hop = max(left[0], left[1]) + max(right[0], right[1])

            return rob, hop

        # res = dfs1(root)
        #
        # return max(res)
        res = max(dfs(root,True),dfs(root,False))
        return res

if __name__ == '__main__':
    solution = Solution()
    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node1 = TreeNode(1, right=node4)
    node2 = TreeNode(2, node1, node3)
    res = solution.rob(node2)
    print(res)
