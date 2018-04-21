from sorting.utils import UNSORTED_100_ITEMS_LIST, get_file_name, bind_function


def sorting(_list):  # O(n2)
    counter = 0
    for i in range(1, len(_list)):
        j = i - 1
        key = _list[i]
        counter += 1
        while _list[j] > key and j >= 0:
            _list[j+1] = _list[j]
            j -= 1
            counter += 1
        _list[j + 1] = key
    print('{} iterations'.format(counter))
    return _list


if __name__ == '__main__':
    func_name = get_file_name(__file__)
    print(func_name)
    func = bind_function(func_name, sorting)
    print(func(UNSORTED_100_ITEMS_LIST))
