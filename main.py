class Node:
    def __init__(self, value):
        self.right: Node | None = None
        self.value = value
        self.left = None | None = None

class BinTree:
    def __init__(self):
        self.root: Node | None = None

    def add_node(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root

        while True:
            if new_node.value < current_node.value:
                if current_node.left is None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
            else:
                break
