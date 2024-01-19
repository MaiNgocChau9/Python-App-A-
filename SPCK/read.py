import os

files = os.listdir("SPCK\\All Notes")
for file in files: 
    print(file)
    file_path = f"SPCK\\All Notes\\{file}"
    with open(file_path, 'r') as file: print(file.read())