"""
Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т. е. последовательность,
состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок."""
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = 0  # Указатель на текущий вложенный список
        self.inner_cursor = -1  # Указатель на элемент внутри списка
        return self

    def __next__(self):
        self.inner_cursor += 1
        while self.cursor < len(self.list_of_list) and self.inner_cursor >= len(self.list_of_list[self.cursor]):
            self.cursor += 1
            self.inner_cursor = 0

        if self.cursor >= len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.cursor][self.inner_cursor]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()