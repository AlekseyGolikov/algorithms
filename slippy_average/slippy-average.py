
# Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
# Измерения велись n секунд.
# В секунду i поступает qi запросов.
# Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

from time import perf_counter
def decor(func):
    def wrapper(*args):
        start = perf_counter()
        func(*args)
        print('Время работы программы: {}'.format(perf_counter() - start))
    return wrapper

@decor
def slip_average(k, n):
    """
        Функция реализует алгоритм скользящего среднего
        k - размер окна
        Пример:
        >>> slipy_average(4, 7)
        [2.5, 3.5, 4.5, 5.5]
    """

    def gen():
        for i in range(1, n+1):
            yield i

    def sum(buffer):
        pass

    def calc(k):
        sum = None
        i = 0
        buffer = []
        while True:
            j = yield sum   # j == (next(g), step)
            buffer.append(j[0])
            if j[1] >= k:
                sum = 0
                for i in range(k):
                    sum += buffer[i]
                else:
                    del_el = buffer.pop(0)
                    sum = float(sum/k)


    c = calc(k)
    next(c)
    g = gen()
    step = 1
    try:
        while True:
            _g = next(g)
            token = (_g, step)
            res = c.send(token)
            if step >= k:
                print(res)
            step += 1
    except StopIteration:
        print("Работа окончена!")

slip_average(4, 7)
