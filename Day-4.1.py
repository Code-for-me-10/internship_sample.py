# snehal Shilvant
# A-55
# day 4 Problem stmt 1
number = (input("number"))
a = number[::-1]
n = int(number)
a =int(a)
first_digit = a%10
last_digit = n%10
if first_digit == last_digit:
    print("last and first digit are same")
else:
    print("last and first digit are not same")


# day 4 Problem stmt 2

NumList = []
Even = []
Odd = []
Prime = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even.append(NumList[j])
    else:
        Odd.append(NumList[j])


def f_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return (0)
    return (1)

for i in NumList:
    if (f_prime(i)):
        Prime.append(i)
Largest = max(NumList)
Smallest = min(NumList)

print("Prime number list is:", Prime)
print("Element in Even List is : ", Even)
print("Element in Odd List is : ", Odd)
print("Smallest number from the list", Smallest)
print("Largest number from the list", Largest)



