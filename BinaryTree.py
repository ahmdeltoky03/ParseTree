class BinaryTree:
    def __init__(self, data):
        self.value = data
        self.left_node = None
        self.right_node = None

    def get_left_child(self):
        return self.left_node

    def get_right_child(self):
        return self.right_node

    def get_root_value(self):
        return self.value

    def set_root_value(self, data):
        self.value = data

    def insert_left(self, data):
        if self.left_node is None:
            self.left_node = BinaryTree(data)
        else:
            temp = BinaryTree(data)
            temp.left_node = self.left_node
            self.left_node = temp

    def insert_right(self, data):
        if self.right_node is None:
            self.right_node = BinaryTree(data)
        else:
            temp = BinaryTree(data)
            temp.right_node = self.right_node
            self.right_node = temp
