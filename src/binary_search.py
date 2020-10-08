def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    print(first, last)
    while first <= last:
        mid = first + (last - first) // 2
        print(mid)
        if item_list[mid] == item:
            return True
        else:
            if item < item_list[mid]:
                last = mid - 1
                print('l', last)
            else:
                first = mid + 1
                print('f', first)
    return False

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13], 13))
