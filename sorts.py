def insert_sort(disordered_list):
    """sort by inserts, O(N^2), смысл в том, что мы берем элемент и вставляем его, если он меньше предыдущего и ведем
    его пока тот не встанет на нужное место """
    for top in range(1, len(disordered_list)):
        itr = top
        while itr > 0 and disordered_list[itr] < disordered_list[itr - 1]:
            disordered_list[itr], disordered_list[itr - 1] = disordered_list[itr - 1],  disordered_list[itr]
            itr -= 1



def choice_sort(disordered_list):
    """sort by choice, O(N^2), смысл в том, что мы выбираем подходящий эелемент на заданную позицию"""
    for pos in range(0, len(disordered_list) - 1):
        for pos_k in range(pos + 1, len(disordered_list)):
            if disordered_list[pos_k] < disordered_list[pos]:
                disordered_list[pos_k], disordered_list[pos] = disordered_list[pos], disordered_list[pos_k]


def bubble_sort(disordered_list):
    """sort by bubble, O(N^2), смысл в том, что по ходу чтения нашего листа мы менянкем местами эелменты и делаем это
    до тех пор пока он не отсортируется """
    for pas in range(1, len(disordered_list)):
        for pas_k in range(0, len(disordered_list) - pas):
            if disordered_list[pas_k] > disordered_list[pas_k + 1]:
                disordered_list[pas_k], disordered_list[pas_k + 1] = disordered_list[pas_k + 1], disordered_list[pas_k]


def count_sort(disordered_list):
    f_list = [0] * (len(disordered_list) + 1)
    """sort by count, O(N), смысл в том, что мы считаем все вхождения числа и потом записываем их по порядку"""
    for elem in disordered_list:
        if not f_list[elem]:
            f_list[elem] += disordered_list.count(elem)
    disordered_list.clear()
    for elem in range(len(f_list)):
        disordered_list += [elem] * f_list[elem]


def test_sorts(sort_alg):
    print('test_case:', sort_alg.__doc__)
    tests_list = [1, 3, 2, 5, 4, 4, 5, 7]
    tests_list_ordered = sorted(tests_list)
    sort_alg(tests_list)
    print(tests_list_ordered)
    print('ok' if tests_list_ordered == tests_list else 'fail')


if __name__ == "__main__":
    test_sorts(insert_sort)
    test_sorts(choice_sort)
    test_sorts(bubble_sort)
    test_sorts(count_sort)