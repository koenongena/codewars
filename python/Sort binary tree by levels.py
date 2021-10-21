class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    queue, path = [], []
    queue.append(node)
    while len(queue) > 0:
        n = queue.pop(0)
        if n is not None:
            path.append(n.value)
            queue.append(n.left)
            queue.append(n.right)

    return path


if __name__ == '__main__':
    print(tree_by_levels(None))
    print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
