from collections import deque


class Node(object):
    def __init__(self, name, flag=False, neighbors=[]):
        self.name = name
        self.flag = flag
        self.neighbors = neighbors

    def __str__(self):
        return self.name

    def __repr__(self):
            return self.name


def find_flag1(n):
    search_queue = deque()
    search_queue.append(n)
    searched = []
    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            searched.append(node)
            if node.flag:
                print('Find {}'.format(node))
                return searched
            [search_queue.append(i) for i in node.neighbors]
    return False


def find_flag2(n):
    res = []
    for i in n.neighbors:
        if i.flag:
            print('{} bingo form {}'.format(i, n))
            res.append((n, i))
            return res
        else:
            res.append(i)
            print('{} from {} empty'.format(i, n))
    for i in n.neighbors:
        if i.neighbors:
            r = find_flag2(i)
            res.append((i, r))
    return res


if __name__ == '__main__':
    n1 = Node('n1')
    n2 = Node('n2')
    n3 = Node('n3')
    n4 = Node('n4')
    n5 = Node('n5')
    n6 = Node('n6', flag=True)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n3, n5]
    n4.neighbors = [n3, n6]
    n5.neighbors = [n6]
    r = find_flag1(n1)
    print(r)
