from sorting.utils import UNSORTED_100_ITEMS_LIST, bind_function, get_file_name


def sorting(_list):  # O(n2)
    changed = True
    counter = 0
    while changed:
        changed = False
        for k, v in enumerate(_list):
            if k + 1 == len(_list):
                break
            if _list[k + 1] < v:
                _list[k], _list[k + 1] = _list[k + 1], v
                changed = True
            counter += 1
    print('{} iterations'.format(counter))
    return _list, counter


if __name__ == '__main__':
    func_name = get_file_name(__file__)
    print(func_name)
    func = bind_function(func_name, sorting)
    print(func(UNSORTED_100_ITEMS_LIST))
