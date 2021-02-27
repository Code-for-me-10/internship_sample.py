# snehal Shilvant
# A-55
# day  4 Problem stmt 3

list = [1, 2, 3,1, (1,3), [1,3], {1,3}, {1,3}, [1,3], [1,3], (1,3), {1,3}, (1,3), {1,3},[1,3],{1,3}]
print(list)
print("list of 1 is :", list.count(1))
print("list of 2 is :", list.count(2))
print("list of 3 is:", list.count(3))

print("list of list is :", list.count([1,3]))
print("list of dictionary is:", list.count({1,3}))
print("list of tuple is:", list.count((1,3)))

