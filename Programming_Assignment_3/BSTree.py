import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BS_tree():
    def __init__(self):
        self.root = None
    def inorder(self, output):      # print the in-order traversal of binary search tree
        # TODO
        def _inorder(node):
            if not node:
                return ""
            else:
                left_child = _inorder(node.left_child)
                right_child = _inorder(node.right_child)
                return left_child + str(node.value) + ' ' + right_child
        result = _inorder(self.root) + '\n'
        output.write(result)
    def preorder(self, output):     # print the pre-order traversal of binary search tree
        # TODO
        def _preorder(node):
            if not node:
                return ""
            else:
                left_child = _preorder(node.left_child)
                right_child = _preorder(node.right_child)
                return str(node.value) + ' ' + left_child + right_child
        result = _preorder(self.root) + '\n'
        output.write(result)
    def postorder(self, output):    # print the post-order traversal of binary search tree
        # TODO
        def _postorder(node):
            if not node:
                return ""
            else:
                left_child = _postorder(node.left_child)
                right_child = _postorder(node.right_child)
                return left_child + right_child + str(node.value) + ' '
        result = _postorder(self.root) + '\n'
        output.write(result)
    def find_max(self, output):     # print the maximum number in binary search tree
        # TODO
        current = self.root
        while current.right_child:
            current = current.right_child
        result = str(current.value) + '\n'
        output.write(result)
    def find_min(self, output):     # print the minimum number in binary search tree
        # TODO
        current = self.root
        while current.left_child:
            current = current.left_child
        result = str(current.value) + '\n'
        output.write(result)
    def insert(self, key):          # insert one node
        # TODO
        if self.root == None:
            self.root = Node(key)
            return
        else:
            current = self.root
            while True:
                if key < current.value:
                    if current.left_child:
                        current = current.left_child
                    else:
                        current.left_child = Node(key)
                        break
                if key > current.value:
                    if current.right_child:
                        current = current.right_child
                    else:
                        current.right_child = Node(key)
                        break
    def delete(self, key):          # delete one node
        # TODO
        def _find_min(node):
            current = node
            while current.left_child:
                current = current.left_child
            return current.value
        def _delete(node, key):
            if not node:
                return None
            elif key < node.value:
                node.left_child = _delete(node.left_child, key)
            elif key > node.value:
                node.right_child = _delete(node.right_child, key)
            else:
                if not node.left_child:
                    return node.right_child
                elif not node.right_child:
                    return node.left_child
                elif node.left_child and node.right_child:
                    right_min_value = _find_min(node.right_child)
                    node.value = right_min_value
                    node.right_child = _delete(node.right_child, right_min_value)
            return node
        self.root = _delete(self.root, key)
    def level(self, output):        # print the height of binary search tree(leaf = 0)
        # TODO
        def _level(node):
            if not node:
                return -1
            else:
                left_height = _level(node.left_child)
                right_height = _level(node.right_child)
                return max(left_height, right_height) + 1
        result = str(_level(self.root)) + '\n'
        output.write(result) 
    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest
        # TODO
        def _internalnode(node):
            if not node or not (node.left_child or node.right_child):
                return ""
            if node.left_child or node.right_child:
                left_child = _internalnode(node.left_child)
                right_child = _internalnode(node.right_child)
                return left_child + str(node.value) + ' ' + right_child
        result = _internalnode(self.root) + '\n'
        output.write(result)
    def leafnode(self, output):     # print the leafnode in BST from left to right
        # TODO
        def _leaf_node(node):
            if not node:
                return ""
            if not node.left_child and not node.right_child:
                return str(node.value) + ' '
            left_child = _leaf_node(node.left_child)
            right_child = _leaf_node(node.right_child)
            return left_child + right_child
        result = _leaf_node(self.root) + '\n'
        output.write(result)
    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # It's important and repeat three times
        #########################
        output = open(output_path, 'w', newline='')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()
if __name__ == '__main__' :
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './input_3.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_3.txt',help="Output file root.")
    args = parser.parse_args()
    
    BS = BS_tree()
    BS.main(args.input, args.output)
    