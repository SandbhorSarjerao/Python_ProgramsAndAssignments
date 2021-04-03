# emptyFileCheck.py

f = open("emptyFile.txt")

if len(f.readlines()) == 0:
    print("Empty File")
else:
    print("Not Empty File")

f.seek(0, 2)
if f.tell() == 0:
    print("Empty File")
else:
    print("Not Empty File")

# ---------------------
cont = f.read()
length_of_file = len(cont)
total_spaces = cont.count(" ")
total_newLines = cont.count("\n")

if length_of_file == total_spaces + total_newLines and length_of_file > 0:
    print("File contains only spaces & newlines only")

f.seek(0, 2)
# if f.tell() > 0:
if cont.isalnum() == True:
    print("Visible Data")
else:
    print("Non Visible Data")