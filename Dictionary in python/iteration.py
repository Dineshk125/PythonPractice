# dic = {
#     "name": "Dinesh",
#     "last_name": "Kumawat",
#     "gender": "Male",
#     "age": 22,
# }

# for k in dic.keys():
#     print(k)  # it print only key that are in dictionary
#     print(dic[k])  # it print values of key in dict.

# for k in dic:
#     print(k)  # it print only key by default

# for v in dic.values():
#     print(v)  # it print values in dictionary.


# print(dic.items())

# """ Q1. print this

# name -> Dinesh
# last_name -> Kumawat
# gender -> Male
# age -> 22

# """

# dic = {
#     "name": "Dinesh",
#     "last_name": "Kumawat",
#     "gender": "Male",
#     "age": 22,
# }

# for k, v in dic.items():
#     print(f"{k} -> {v}")

# """Q2. print sum of all subjects."""

# dic = {"physics": 66, "che": 60, "math": 90, "eng": 89, "hindi": 96}

# total_sum = 0

# for sum in dic.values():
#     total_sum += sum
# print(total_sum)

# for k in dic.keys():
#     print(k)

# for v in dic.values():
#     print(v)

# for k, v in dic.items():
#     print(f"{k} -> {v}")

# """
# Q.3 Ask sub name and marks from the user and keep adding it to dictionary.


#     Enter the number of subjects: 4

# Enter the subject name: Maths

# Enter the marks for Raths: 22

# Enter the subject name: English

# Enter the marks for English: 90

# Enter the subject name: Computer

# Enter the marks for Computer: 87

# Enter the subject name: Science

# Enter the marks for Science: 66

# #Output ('Maths: 22.0, 'English': 90.0, 'Computer': 87.0, 'Science': 66.0)

# """

# marks = {}

# total_sub = int(input("Enter total number of Subjects: "))

# for i in range(0, total_sub):
#     sub_name = input("Enter subject name = ")
#     sub_marks = int(input(f"Enter subject marks for {sub_name} = "))
#     marks[sub_name] = sub_marks
#     # marks.update({sub_name: sub_marks})
# print(marks)

# """
# Q4. Convert two lists into a dictionary. Make two list on your own of same length, and convert them to dictionary.

# ...

# lst1= ['Ten', 'Twenty', 'Thirty']

# 1st2 [10, 20, 30]

# # Output

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30)

# """
# lst1 = ["Ten", "Twenty", "Thirty"]

# lst2 = [10, 20, 30]

# dic = {}

# for l1 in range(0, len(lst1)):
#     # for l2 in range(l1, l1 + 1):
#     # dic.update({lst1[l1]: lst12[l2]})
#     dic.update({lst1[l1]: lst2[l1]})
# print(dic)

# """

# Q5. Write a Python program to sum all the items in a dictionary.


# """

# dic = {
#     "math": 90,
#     "Science": 89,
# }

# print(f"{sum(list(dic.values()))}")

# """ Q6. Write a Python program to multiply all the items in a dictionary. """
# dic = {
#     "math": 9,
#     "Science": 8,
# }
# m = 1
# for i in dic.values():
#     m = m * i

# print(m)

# """
# Q7. Ask a string from user. Display the dictionary where each key is a character and
#     value is the frequency of that character that comes in that string.

# Enter a string: hello world

# # Output

# ('h': 1, 'e': 1, '1': 3, 'o': 2, ': 1, 'w': 1, 'r': 1, 'd': 1)

# """

# s = input("Enter a string: ")

# dic = {}
# # # Method 1

# # for i in range(0, len(s)):
# #     v = s.count(s[i])
# #     dic.update({s[i]: v})
# # print(dic)

# ## Method 2

# for i in range(0, len(s)):
#     v = s.count(s[i])
#     if s[i] != dic.keys():
#         dic.update({s[i]: v})
# print(dic)

# """
# Q147. Store "name" of a student as Key, "list of 5 marks" of that student as a Value.
#       Store atleast 5 student names. Print the sum and percentage of all the students.

# ...

# students dict(

# "Student1": 185, 90, 78, 92, 88],.

# "Student2": [75, 88, 92, 80, 87),

# "Student3": [90, 95, 89, 78, 93],

# "Student4": [80, 85, 88, 92, 871,

# "Students": [92, 83, 95, 90, 55]

# +

# Studenti Sum: 433, Percentage: 86.60%

# Student2 Sum: 422, Percentage: 84.40%

# Student3 Sum: 445, Percentage: 89.00%

# Student4 Sum: 432, Percentage: 86.40%

# Students Sum: 450, Percentage: 90.00%

# """

# dic = int(input("Enter student Number = "))
# dic2 = {}

# for i in range(1, dic + 1):
#     student = input("Enter student name = ")
#     l = []
#     for j in range(1, 6):
#         st_marks = int(input(f"Enter {student} marks = "))
#         l.append(st_marks)
#         dic2.update({student: l})
# print(f"{dic2}")

# s = 0
# p = 1
# for k, v in dic2.items():
#     s = sum(v)
#     p = (s / 500) * 100
#     print(f"The sum of {k} marks is = {s} and the total percentage of {k} is ={p}%")


# """
# Q148. Store marks of 5 different subjects in a dictionary. Ask subject name as an input from the User.
#       Print the marks of that subject entered by User. If subject does not exist, print "Invalid".


# """


# dic = {
#     "english": 90,
#     "hindi": 70,
#     "math": 92,
#     "science": 94,
#     "Sscience": 80,
# }

# dic2 = input("Enter subject name: ")

# if dic2 in dic:
#     print(dic.get(dic2))
# else:
#     print("INVALID INPUT SUBJECT")
