# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test():
    """
    Функция получает аргументы маркера теста и выводит на печать без кортежных скобок
    """
    result = test.pytestmark[0].args
    print('\n' + str(result)[1: -1])
    pass
