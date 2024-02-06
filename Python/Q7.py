class BST:
    def __init__(self, value):
        self.leftChild = None
        self.parent = value
        self.rightChild = None
        # definition of the BST type

    def addTree(self, value):
        if value <= self.parent:
            # checks where the new node should go
            if self.leftChild:
                # if there is already a node go even deeper
                return self.leftChild.addTree(value)
            else:
                # if there isn't a node set it to the value
                self.leftChild = BST(value)
                return
        else:
            # if the node isn't on the left it goes on the right
            if self.rightChild:
                # if there is already a node go even deeper
                return self.rightChild.addTree(value)
            else:
                # if there isn't a node set it to the value
                self.rightChild = BST(value)
                return

    def printTree(self):
        if self.leftChild:
            self.leftChild.printTree()
        print(self.parent)
        if self.rightChild:
            self.rightChild.printTree()
    # tree is printed in order


root = BST(0)
first = True
print("Enter the integers\n")
print("To exit entering input ;\n")
while True:
    temp = input("Enter:\n")
    if temp == ';':
        break
    else:
        temp = int(temp)
        if first == True:
            # if root isn't set it will set it
            first = False
            root = BST(temp)
        else:
            root.addTree(temp)

root.printTree()
