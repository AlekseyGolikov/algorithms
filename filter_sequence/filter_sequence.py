
def filter_sequence(seq):
    """
        Программа преобразует входную последовательность целых чисел, в которой могут быть вложенные списки,
        в простой список
        >>> filter_sequence([1, 2, [3, 4], [5, [6, 7]], 8, [9, 10]])
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    def filter(_seq):
        for x in _seq:
            if not isinstance(x, int):
                yield from filter(x)
            else:
                yield x

    res = []
    _f = filter(seq)
    try:
        while True:
            res.append(next(_f))
    except StopIteration:
        print(res)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)