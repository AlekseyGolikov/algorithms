"""
    Пример использования структуры данных "стэк" LIFO

    Есть еще одна вещь, на которую следует обратить внимание. Все наши методы должны иметь
    постоянную временную сложность — O(1). Это означает, что их работа должна занимать одинаковое время,
    независимо от длины стека. Если бы нам пришлось, к примеру, перебирать список в цикле,
    временная сложность была бы O(n), где n — длина списка. Но нам ничего такого делать не пришлось,
    так что все в порядке.
"""
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def __str__(self):
        return str(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
print(s.pop())
print(s)