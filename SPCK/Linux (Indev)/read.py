# import os

# files = os.listdir("SPCK\\All Notes")
# for file in files: 
#     print("Tên ghi chú:",file)
#     file_path = f"SPCK\\All Notes\\{file}"
#     with open(file_path, 'r') as file: print("Nội dung:",file.read())

# import os
# duong_dan = os.path.join("SPCK\\All Notes", "ten_file.txt")
# with open(duong_dan, 'w', encoding='utf-8') as file: file.write("Đây là file mới")

local_item = [1,4,3,5]
local_item.sort()
print(local_item)