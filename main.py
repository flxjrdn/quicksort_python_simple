
import numpy as np


def quicksort(number_list, index_left, index_right):
    if (index_left < index_right) & (index_left >= 0):
        number_list, index_partition = partition(number_list, index_left, index_right)
        number_list = quicksort(number_list, index_left, index_partition - 1)
        number_list = quicksort(number_list, index_partition, index_right)
    return number_list


def partition(number_list, index_left, index_right):
    index_p = index_left - 1
    for i in range(index_left, index_right):
        if number_list[i] <= number_list[index_right]:
            index_p += 1
            swap(number_list, index_p, i)
    index_p += 1
    swap(number_list, index_p, index_right)
    return number_list, index_p


def swap(number_list, index_a, index_b):
    number_list[index_a], number_list[index_b] = number_list[index_b], number_list[index_a]
    return number_list


if __name__ == '__main__':
    num_elements = 20
    sort_list = np.random.randint(0, 10, size=(num_elements,))
    sort_list = quicksort(sort_list, 0, num_elements - 1)

    print('sorted list:  ', sort_list)
