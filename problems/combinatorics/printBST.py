def print_bst(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_bst(root.left, level + 1, "L--> ")
            else:
                print(" " * ((level + 1) * 4) + "L--> None")
            
            if root.right:
                print_bst(root.right, level + 1, "R--> ")
            else:
                print(" " * ((level + 1) * 4) + "R--> None")