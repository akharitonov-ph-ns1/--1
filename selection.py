def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if list[j] < list[min_i]:
                min_i = j
        list[i], list[min_i] = list[min_i], list[i]
