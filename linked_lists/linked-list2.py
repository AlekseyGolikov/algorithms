"""
    Программа реализует пример двунаправленной очереди (двунаправленного связанного списка).
    вход: создается внунаправленная очередь <1> -> <2> -> <3> -> <4> -> <5>
    выход: компилятор пробегается по созданной очереди вперед и назад
    1 -> 2 -> 3 -> 4 -> 5 -> 4 -> 3 -> 2 -> 1
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def append(self, val):
        end = Node(val)
        n = self
        while n.next:
            n = n.next
        end.prev = n
        n.next = end


if __name__ == '__main__':
    l = Node(1)

    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)

    node = l
    print(node.data)
    c = '+'
    while True:
        if node.next and c == '+':
            node = node.next
            print(node.data)
        else:
            c = '-'
        if node.prev and c == '-':
            node = node.prev
            print(node.data)
        if node.prev == None and c == '-':
            break