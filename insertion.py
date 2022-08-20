def insertion_sort(array):
    for p in range (0, len(array)):
        elemento_atual = array[p]

        while p > 0 and array [p-1] > elemento_atual:
            array[p] = array [p -1]
            p -= 1

        array[p] = elemento_atual

vetores = [3,1,5,9,21,33,55,51,13,19,41,47,33,31,25,39,91,93,103,43,61,69,63,77,127,133,199,207,99]

insertion_sort(vetores)
print(vetores)
