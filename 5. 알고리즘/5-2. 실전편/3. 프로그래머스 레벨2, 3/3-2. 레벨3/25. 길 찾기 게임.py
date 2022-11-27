import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, coord):
        self.coord = coord
        self.left = None
        self.right = None

    def __str__(self):
        return "<" + str(self.coord[0]) + ', ' + str(self.coord[1]) + ">"


def make_left_sub_nodes_go(root_node_coord, rest_nodes):
    return list(filter(lambda coord: coord[0] < root_node_coord[0], rest_nodes))


def make_right_sub_nodes_go(root_node_coord, rest_nodes):
    return list(filter(lambda coord: coord[0] > root_node_coord[0], rest_nodes))


def create_tree(root_node, rest_nodes):
    if len(rest_nodes) >= 2:
        # L R
        if root_node.coord[0] > rest_nodes[0][0] and root_node.coord[0] < rest_nodes[1][0]:
            root_node.left = create_tree(Node(rest_nodes[0]), make_left_sub_nodes_go(root_node.coord, rest_nodes[2:]))
            root_node.right = create_tree(Node(rest_nodes[1]), make_right_sub_nodes_go(root_node.coord, rest_nodes[2:]))
        # L
        elif root_node.coord[0] > rest_nodes[0][0] and root_node.coord[0] > rest_nodes[1][0]:
            root_node.left = create_tree(Node(rest_nodes[0]), rest_nodes[1:])
        # R
        elif root_node.coord[0] < rest_nodes[0][0]:
            root_node.right = create_tree(Node(rest_nodes[0]), rest_nodes[1:])
    elif len(rest_nodes) == 1:
        # L
        if root_node.coord[0] > rest_nodes[0][0]:
            root_node.left = create_tree(Node(rest_nodes[0]), rest_nodes[1:])

        # R
        elif root_node.coord[0] < rest_nodes[0][0]:
            root_node.right = create_tree(Node(rest_nodes[0]), rest_nodes[1:])
    else:
        root_node

    return root_node


def pre_order(root, result):
    result.append(root.coord[2])
    if root.left is not None:
        pre_order(root.left, result)
    if root.right is not None:
        pre_order(root.right, result)


def post_order(root, result):
    if root.left is not None:
        post_order(root.left, result)
    if root.right is not None:
        post_order(root.right, result)
    result.append(root.coord[2])


def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i] = nodeinfo[i] + [i + 1]
    nodeinfo.sort(key=lambda node: (node[1], -node[0]), reverse=True)
    root_node = Node(nodeinfo[0])
    root_node = create_tree(root_node, nodeinfo[1:])
    pre_result = []
    pre_order(root_node, pre_result)
    post_result = []
    post_order(root_node, post_result)
    # print(pre_result)
    # print(post_result)
    answer.append(pre_result)
    answer.append(post_result)
    return answer