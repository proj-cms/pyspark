# Special thanks to code basics for making DSA so easy

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        # this method will be required to add child
        if self.data == data:
            return  # this data node already exists

        if data < self.data:
            if self.left:  # means this node has left data node , so we have to check of left side node should be added
                self.left.add_child(data)
            else:  # if left node does not exist
                self.left = BinarySearchTree(data)
        else:
            if self.right:  # means this node has right data node , so we have to check of left side node should be
                # added
                self.right.add_child(data)
            else:  # if left node does not exist
                self.right = BinarySearchTree(data)

        return

    def search_tree(self, data):
        if self.data == data:
            return True

        if data < self.data:  # traverse left sub tree
            if self.left:
                return self.left.search_tree(data)
        else:
            # traverse right subtree
            if self.right:
                return self.right.search_tree(data)

        return False

    def in_order_traversal(self):
        # left-root-right
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # root-left-right
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        # root-left-right
        elements = []

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        elements.append(self.data)

        return elements


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    # iterate over the list
    for index in range(1, len(elements)):
        root.add_child(elements[index])

    return root


if __name__ == "__main__":
    # countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    print("Pre order traversal gives this :", numbers_tree.pre_order_traversal())
    print("Pre order traversal gives this :", numbers_tree.post_order_traversal())
