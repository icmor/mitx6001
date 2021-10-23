from random import randint


def bisection_search(l: list, e: int) -> int:
    if not l: return False
    lower = 0
    upper = len(l) - 1
    while True:
        middle = (lower + upper) // 2
        val = l[middle]
        if e == val:
            return True
        if lower == upper:
            return False
        if e > val:
            lower = middle + 1
        else:
            upper = middle - 1


def bubble(l: list) -> list:
    assert l, "Empty list"
    s = l[:]
    count = 1
    swap = True
    while swap:
        swap = False
        for i in range(0, len(s)-count):
            if s[i] > s[i+1]:
                swap = True
                s[i], s[i+1] = s[i+1], s[i]
        count += 1
    return s


def selection(l: list) -> list:
    assert l, "Empty list"
    s = l[:]
    for i in range(len(s)-1):
        min_indx = i
        min_val = s[i]
        for j in range(i+1, len(s)):
            if s[j] < min_val:
                min_indx = j
                min_val = s[j]
        s[i], s[min_indx] = min_val, s[i]
    return s


def merge_sort(l: list) -> list:
    def merge(l1, l2):
        i = j = 0
        s = []
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                s.append(l1[i])
                i += 1
            else:
                s.append(l2[j])
                j += 1
        if j < len(l2):
            s += l2[j:]
        else:
            s += l1[i:]
        return s

    def sort(l):
        if len(l) < 2: return l
        l1 = sort(l[:len(l)//2])
        l2 = sort(l[len(l)//2:])
        return merge(l1, l2)

    assert l, "Empty list"
    return sort(l)

l = [randint(0, 100_000) for x in range(10_000)]
