
L = [(2,3, 25), (1,4, 20), (3,1, 5)]
print("List :", L)


print("Sorting according to last element")
def second_last_ele_sort(t):
    return t[2]


L.sort(key=second_last_ele_sort)
print(L)
print("Sorting according to second last element")
def first_ele_sort(t):
    return t[1]


L.sort(key=first_ele_sort)
print(L)
print("Sorting according to first element")
def first_ele_sort(t):
    return t[0]


L.sort(key=first_ele_sort)
print(L)
