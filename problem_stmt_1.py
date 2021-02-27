# problem statement 1
p = int(input("Enter principal amount : "))
r = float(input("Enter Rate of interest:"))
n = int(input("Enter time:"))
A = p*(1+r/100)**n
print("compound interest :", A)


# problem stmt 2
Weight = [70, 80, 45, 50]
print(Weight)
maximum_variable = max(Weight)
print(maximum_variable)
Weight.remove(45)
Weight.append(48)
print(Weight)
sum = sum(Weight)

print("sum of Weight:", sum)
mean = sum/4
print("Mean of the all Weights", mean)