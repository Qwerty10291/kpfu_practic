class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

def printTree(root):
    if not root:
        return
    print(root.val)
    printTreeRecursive(root, 1)

def printTreeRecursive(node, depth):
    if not node:
        return
    for i in range(len(node.children) - 1):
        print("  " * depth, end="")
        print("|--", node.children[i].val, sep="")
        printTreeRecursive(node.children[i], depth + 1)
    if node.children:
        print("  " * depth, end="")
        print("`--", node.children[-1].val, sep="")
        printTreeRecursive(node.children[-1], depth + 1)

root = TreeNode("A", [
    TreeNode("B", [
        TreeNode("C", [
        ]),
        TreeNode("D", [
            TreeNode("F", [])
        ]),
        TreeNode("J", [])
    ]),
    TreeNode("E", [
        TreeNode("C", [])
        ]
    )
])

printTree(root)