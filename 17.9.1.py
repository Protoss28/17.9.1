array = list(map(int, input('Ввести числа через пробел: ').split()))

print(array)

element = int(input('Ввести  число в рамках последовательности: '))
while element:
    if element not in range(min(array) + 1, max(array)):
        print('Некорректное число')
        element = int(input('Ввести последовательно число: '))
    else:
        break

def array_sort(array, element, is_in_list):
    for i in range(len(array)):  
        if array[i] == element:
            is_in_list = True
        idx_min = i  
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:  
            array[i], array[idx_min] = array[idx_min], array[i]


def binary_search(array, element, left, right):
    if left > right:
        return right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

is_in_list = False
array_sort(array,element,is_in_list)

a = (binary_search(array, element, 0, len(array) - 1))
if a == 0:
    print("Минимальное число в списке")
elif is_in_list:
    print(a-1) 
else:
    print(a) 