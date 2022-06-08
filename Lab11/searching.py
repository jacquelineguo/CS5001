'''
Xuan Guo
CS5001, Fall 2020

Lab11: Recursive binary search
'''


def binary_search(lst, item):
    '''
        Function -- binary_search
        Parameters:
            lst -- The list to search in.
            item -- The item to search for.
        Returns:
            True if the item is in the list, False otherwise.
    '''
    if lst == None or len(lst) == 0:
        return False
    mid = len(lst) // 2
    if lst[mid] == item:
        return True
    elif lst[mid] < item:
        return binary_search(lst[(mid) + 1 : len(lst)], item)
    else:
        return binary_search(lst[0 : (mid)], item)

def bsearch(lst):
    def binary_search_shifted(lst, left, right):
        if right < left:
            return lst[0]
        if right == left:
            return lst[left]
        mid = (left + right) // 2
        if mid < right and lst[mid + 1] < lst[mid]:
            return lst[mid + 1]
        if mid > left and lst[mid] < lst[mid - 1]:
            return lst[mid]
        if lst[right] > lst[mid]:
            return binary_search_shifted(lst, left, mid - 1)
        return binary_search_shifted(lst, mid + 1, right)            
    return binary_search_shifted(lst, 0, len(lst) - 1)


def main():
    lst = [3, 4, 5, 6, 7, 1, 2]
    # print(binary_search(lst, 1))
    print(bsearch(lst))

if __name__ == "__main__":
    main()