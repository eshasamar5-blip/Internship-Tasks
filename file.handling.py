with open("notes.txt", "w")as f:
    f.write ("My name is Esha Samar")
    f.write("My fathers name is Muhammad Nawab")

with open ("notes.txt", "r")as f:
    for line in f:
        print(line.strip())

with open("notes.txt", "a")as f:
    f.write ("\nBS Artificial Intelligence\n")

with open ("notes.txt","r")as f:
    content=f.read()
    print (content)