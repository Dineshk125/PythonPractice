# import os

# if os.path.exists("method.txt"):
#     os.rename("method.txt", "New_method.txt")
#     print("File Renamed.")
# else:
#     print("File not exists.")

with open("new_method.txt", "a") as f:
    f.write("\n Hii i am dinesh")

    x = f.read(5)
    print(x)
