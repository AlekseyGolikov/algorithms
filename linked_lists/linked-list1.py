"""
    Пример реализации однонаправленной очереди (связанного списка)
"""
class Node:

    def __init__(self, data):
        self._data = data
        self._next = None

    def append(self, val):
        _end = Node(val)    # указатель на конечный элемент списка
        n = self            # указатель на текущий элемент списка
        while n._next:      # пробегаем к концу очереди
            n = n._next
        n._next = _end

if __name__ == '__main__':
    l = Node('aaa')
    l.append('bbb')
    l.append('ccc')
    l.append('ddd')
    l.append('eee')

    node = l
    print(node._data)
    while node._next:
        node = node._next
        print(node._data)
