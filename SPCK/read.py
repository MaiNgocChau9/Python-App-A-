# import os

# files = os.listdir("SPCK\\All Notes")
# for file in files: 
#     print(file)
#     file_path = f"SPCK\\All Notes\\{file}"
#     with open(file_path, 'r') as file: print(file.read())

import os
all_task = []

with open("SPCK\\data\\todo_list.ecl", 'r') as file: 
    all_task = file.read().splitlines()
    print(a)