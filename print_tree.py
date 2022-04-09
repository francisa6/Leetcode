from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    val: int
    left: Optional[Node] = None
    right: Optional[Node] = None


my_tree = Node(10, left=Node(5, left=Node(3),), right=Node(15, right=Node(20)))


def recurse(node: Node, result: List[int]):
    if node.left is not None:
        recurse(node.left, result)
    result.append(node.val)
    if node.right is not None:
        recurse(node.right, result)


def to_list(node: Node) -> List[int]:
    result = []
    recurse(node, result)
    return result


print(to_list(my_tree))


def stackVersion(node: Node):
    stack = [node]
    result = []
    while len(stack) > 0:

        node = stack.pop()

        if isinstance(node, int):
            result.append(node)
        else:
            if node.right:
                stack.append(node.right)

            stack.append(node.val)

            if node.left:
                stack.append(node.left)

    return result


def stackVersion2(node: Optional[Node]):
    result: List[int] = []
    stack: List[Node] = []
    while node is not None:
        stack.append(node)
        node = node.left
        while node is None and len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            node = node.right
    return result


print(stackVersion2(my_tree))
