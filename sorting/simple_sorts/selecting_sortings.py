from sorting.utils import UNSORTED_100_ITEMS_LIST, bind_function, get_file_name


def sorting(_list):  # O(n2)
    counter = 0
    for index, value in enumerate(_list):
        min_index = min(range(index, len(_list)), key=_list.__getitem__)
        _list[index], _list[min_index] = _list[min_index], value
        counter += 1
    print('{} iterations'.format(counter))
    return _list


if __name__ == '__main__':
    func_name = get_file_name(__file__)
    print(func_name)
    func = bind_function(func_name, sorting)
    print(func(UNSORTED_100_ITEMS_LIST))
