
class SlippyAverage:
    """
        Класс реализует метод скользящего среднего для глубины окна усреднения k
    """
    def __init__(self):
        self.__coro = self.average_seq()

    def __enter__(self):
        x = self.__coro.__next__()
        # print(type(x))               # class 'float'
        # print(type(self.__coro))     # class 'generator'
        return self.__coro

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__coro.close()

    def send(self, token):
        return self.__coro.send(token)

    def average_seq(self):
        buffer = []
        _sum = 0.0
        while True:
            token = yield _sum  # token = (k, step)
            buffer.append(token[1])
            if token[1] >= token[0]:
                _sum = float(sum(buffer) / token[0])
                del_el = buffer.pop(0)

if __name__ == '__main__':
    k = 4
    res = []
    with SlippyAverage() as av:
        for i in range(1, 8):
            token = (k, i)
            _res = av.send(token)
            if i >= 4:
                res.append(_res)
        else:
            print(res)
