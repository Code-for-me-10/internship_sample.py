list = [1,2,4,12,6,3,24,5,20,8,3,10,22,54,87,90]
L1 = []
L2 = []
print(list)
print(len(list))
value = int(len(list)/2)
median = list[value]
print("meadian is", median)
for i in list:
    if i > median:
        L1.append(i)
    else:
        L2.append(i)
print("Elements Greater than median", L1)
print("Elements Smaller than median", L2)



