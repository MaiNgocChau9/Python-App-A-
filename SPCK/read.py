import os

files = os.listdir("SPCK\\All Notes")
for file in files: 
    print("Tên ghi chú:",file)
    file_path = f"SPCK\\All Notes\\{file}"
    with open(file_path, 'r') as file: print("Nội dung:",file.read())