def tree(root_label,branches=[]):
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in  branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def right_binarize(tree):
    """根据 tree 构造一个右分叉的二叉树"""
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

right_binarize([1, 2, 3, 4, 5, 6, 7])
