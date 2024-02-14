class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left: TreeNode = None
        self.right: TreeNode = None


class BinaryTree:

    @staticmethod
    def insert_level_order(val, root):
        new_node = TreeNode(val)
        if root is not None:
            queue: list[TreeNode] = [root]

            while len(queue) > 0:
                temp_node = queue.pop(0)
                if not temp_node.left:
                    temp_node.left = new_node
                    break
                else:
                    queue.append(temp_node.left)

                if not temp_node.right:
                    temp_node.right = new_node
                    break
                else:
                    queue.append(temp_node.right)
            return root
        else:
            return TreeNode(val)

    @staticmethod
    def inorder(n: TreeNode):
        if not n:
            return
        BinaryTree.inorder(n.left)
        print(n.data)
        BinaryTree.inorder(n.right)

    @staticmethod
    def level_order(root: TreeNode):
        queue: list[TreeNode] = [root]
        while len(queue) > 0:
            tmp = queue.pop(0)
            print(tmp.data)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)


root = BinaryTree.insert_level_order(1, None)

for i in range(2, 8):
    root = BinaryTree.insert_level_order(i, root)

BinaryTree.level_order(root)
