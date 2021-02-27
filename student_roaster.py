# Snehal Shilvant
# A-55
# day_7

Class_1 = ["Amit Sharma", "Jaspal Singh", "Shekhar Kumar", "Yashoda Naik"]
Class_2 = ["Hiten Patel", "Gauri Sharma", "Chetan Nitave"]
New_class = Class_1 + Class_2

# Printing concatenated list
print("Class_3 is : " + str(New_class))

New_class.append("Priti patel")
print("new class is")
print(New_class)

New_class.remove("Yashoda Naik")
print("New Updated List is:", New_class)

# Let's create a dictionary for Jaspal Singh in each subject to generate his progress report.

course = {"Maths": 65, "English": 70, "History": 80, "Hindi": 70, "Science": 60 }

print("Marks of all subject", course)
total = sum(course.values())
print("total marks obtained :", total)
Percentage = (total/500)*100
print("percentage of jaspal singh is:", Percentage, "%")


# find topper

Mathematics = {"Amit Sharama":78,"Jaspal Singh":95,"Shekhar Kumar":65,"Hiten Patel":50,"Gauri Sharama":70,"Chetan Nitave":66,"priti Patil":66}
print("marks of mathematics of all students", Mathematics)
Topper = max(Mathematics, key=Mathematics.get)
print(Topper)
First_name , Last_name = Topper.split()
print("First name is :", First_name)
print("Last name is :", Last_name)
print("full Name is :")
Full_name = " ".join([First_name, Last_name])
print(Full_name)
Certificate_name = Full_name.upper()
print("Certificate name :-", Certificate_name)


