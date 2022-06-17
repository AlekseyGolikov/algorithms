"""
    Программа реализует алгоритм обхода простейшего бинарного дерева.
    Дерево - это структура данных, каждый элемент которого указывает на несколько других узлов.
    Бинарным называется такое дерево, узлы которого содержат в себе ссылки не более чем на 2 других узла
    Используемый пример дерева:
          1           При прямом обходе мы посещаем родительские узлы до посещения узлов-потомков.
        /   \      В случае с нашим деревом мы будем обходить узлы в таком порядке: 1, 2, 4, 5, 3.
      2      3        Обратный обход двоичного дерева — это когда вы сначала посещаете узлы-потомки,
     / \           а затем — их родительские узлы. В нашем случае порядок посещения узлов при обратном обходе будет таким:
    4   5          4 5 2 3 1
    При центрированном обходе мы посещаем все узлы слева направо. Центрированный обход нашего дерева —
    это посещение узлов 4, 2, 5, 1, 3.
    Источник: https://pythonist.ru/obhod-dvoichnogo-dereva-na-python/?ysclid=l4i1nmbae4462654408
"""
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.right = None   # указатель на правый узел
        self.left = None    # указатель на левый узел

def pre_order(node):
    """
        Реализация прямого (pre-order) обхода бинарного дерева
        Вывод: 1 2 4 5 3
    """
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    """
        Реализация обратного (post-order) обхода бинарного дерева
        Вывод: 4 5 2 3 1
    """
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)

def in_order(node):
    """
        Реализация центрического (in-order) обхода бинарного дерева.
        Вывод: 4 2 5 1 3
    """
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    pre_order(tree)
    # post_order(tree)
    # in_order(tree)