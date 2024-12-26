'''
Написать итератор, аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности.
'''
from collections import deque

# Мой первый вариант
# class FlatIterator:
#     def __init__(self, list_of_list):
#         self.list_of_list = list_of_list
#
#     def __iter__(self):
#         self.stack = [(self.list_of_list, 0)]
#         return self
#
#     def __next__(self):
#         while self.stack:
#             current_list, current_index = self.stack[-1]
#             if current_index >= len(current_list):
#                 current_index += 1
#                 self.stack.pop()
#                 continue
#             self.stack[-1] = (current_list, current_index + 1)
#             item = current_list[current_index]
#             if isinstance(item, list):
#                 self.stack.append((item, 0))
#             else:
#                 return item
#         raise StopIteration

#Второй вариант
class FlatIterator:
    def __init__(self, list_of_lists):
        self.queue = deque(list_of_lists)

    def __iter__(self):
        return self

    def __next__(self):
        while self.queue:
            current_item = self.queue.popleft() # Берём элемент из начала очереди
            if isinstance(current_item, list):
                self.queue.extendleft(reversed(current_item)) # Добавляем вложенные списки в начало
            else:
                return current_item
        raise StopIteration





def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    # l = [
    #     [['a'], ['b', 'c']],
    #     ['d', 'e', [['f'], 'h'], False],
    #     [1, 2, None, [[[[['!']]]]], []]
    # ]
    # print(list(FlatIterator(l)))
    test_3()