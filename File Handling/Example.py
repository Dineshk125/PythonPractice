f_name = input("Enter a file name (Without Extention) : ")
f_name = f_name + ".txt"

with open(f_name, "w") as f:
    while True:
        text = input("Enter a text: ")
        if text == "q" or text == "q":
            break
        f.write(text)
        f.write("\n")
