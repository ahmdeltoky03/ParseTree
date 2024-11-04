from Stack import Stack
from BinaryTree import BinaryTree


def build_parse_tree(expr):
    # fully parenthesized expression + white spaces
    tokens = expr.split()

    tree = BinaryTree("")
    stack = Stack()
    curr = tree
    stack.push(tree)  # tree == curr

    for token in tokens:

        if token == "(":
            # token == left parenthesis
            # insert left node
            # push curr in stack
            # update curr
            curr.insert_left("")
            stack.push(curr)
            curr = curr.get_left_child()
        elif token == ")":
            # token == right parenthesis
            # Go back one step
            # curr = stack.pop()
            curr = stack.pop()
        elif token in ["+", "-", "/", "*"]:
            # token == operator
            # set root_value with operator
            # create right_node
            # push curr in stack
            # update curr
            curr.set_root_value(token)
            curr.insert_right("")
            stack.push(curr)
            curr = curr.get_right_child()
        else:
            # token == operand
            # set root_value with operand
            # Go back one step (pop from stack)
            curr.set_root_value(token)
            curr = stack.pop()
    # print('Tree is built')
    return tree


def post_order(tree):
    if tree is not None:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_value(), end=" ")


if __name__ == "__main__":
    pt_1 = build_parse_tree(" ( ( A + ( B * C ) ) - ( ( D / E ) * F ) ) ")
    pt_2 = build_parse_tree("( ( 10 + 5 ) * 3 )")
    post_order(pt_1)
    print('')
    post_order(pt_2)
